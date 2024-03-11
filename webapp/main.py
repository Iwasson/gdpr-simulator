import time
import statistics

from flask import Flask, render_template, request, jsonify
from .functions.database_seeder import seed_db
from .functions.sqlite_wrapper import (
    get_first_n_rows,
    remove_links,
    get_link_data,
    get_table_schema,
    explain_delete_command,
    delete_transactions,
)

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home_page.html"), 200


@app.route("/generate", methods=["POST"])
def generate_schema():
    start_time = time.time()
    num_columns = int(request.form["num_columns"])
    num_rows = int(request.form["num_rows"])
    linking_strength = int(request.form["linking_strength"])
    link_deviation = int(50 - linking_strength / 100 * 50)
    schema, links = seed_db(num_rows, num_columns, link_deviation)
    links_sorted = sorted(set(links))
    top_rows = get_first_n_rows(10)
    end_time = time.time()

    time_diff_count = end_time - start_time
    time_diff = f"{time_diff_count:.2f} Seconds"

    return (
        render_template(
            "display.html",
            num_columns=num_columns,
            num_rows=num_rows,
            link_deviation=link_deviation,
            schema=schema,
            top_rows=top_rows,
            time_diff=time_diff,
            links=links,
            links_sorted=links_sorted,
        ),
        200,
    )


@app.route("/delete_rows", methods=["POST"])
def delete_data():
    start_time = time.time()
    link = int(request.form["link_value"])
    row_count = int(request.form["row_value"])
    rows = get_link_data(link)
    schema = get_table_schema()
    remove_links(link)
    end_time = time.time()

    time_diff_count = end_time - start_time
    time_diff = f"{time_diff_count:.2f} Seconds"
    return (
        render_template(
            "delete.html",
            link=link,
            time_diff=time_diff,
            row_count=row_count,
            rows=rows,
            schema=schema,
        ),
        200,
    )


@app.route("/explain_delete_rows", methods=["GET"])
def explain_delete():
    link = request.args.get('link_value_2')
    explain = explain_delete_command(link)

    return jsonify({"message" : explain})


@app.route('/delete_transactions', methods=['POST'])
def transaction():
    start_time = time.time()
    link = int(request.form["link_value_3"])
    num = int(request.form["delete_count"])
    times = delete_transactions(link, num)
    end_time = time.time()
    time_diff_count = end_time - start_time
    time_diff = f"{time_diff_count:.2f} Seconds"

    total_time = sum(times)
    average_time = total_time / len(times)
    max_time = max(times)
    min_time = min(times)
    deviation = "N/A"
    if len(times) > 2:
        deviation = statistics.stdev(times)

    return (
        render_template(
            "delete_multiple.html",
            link=link,
            num=num,
            average_time=average_time,
            time_diff=time_diff,
            deviation=deviation,
            max_time=max_time,
            min_time=min_time,
        )
    )