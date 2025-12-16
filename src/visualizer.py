from bokeh.plotting import figure, show
from bokeh.layouts import row
from bokeh.models import Legend

def plot_results(train_df, test_df, mapped_df):

    p_train = figure(
        title="Training Data",
        x_axis_label="x",
        y_axis_label="y",
        width=400,
        height=350
    )

    train_cols = [c for c in train_df.columns if c != "x"]
    colors = ["navy", "green", "red", "orange"]  # 4 colours for y1–y4

    legend_items = []
    for col, color in zip(train_cols, colors):
        r = p_train.line(
            train_df["x"],
            train_df[col],
            line_width=2,
            color=color
        )
        legend_items.append((col, [r]))

    legend = Legend(items=legend_items, location="top_left")
    p_train.add_layout(legend, "right")
    p_train.legend.click_policy = "hide"

    p_test = figure(
        title="Test Data",
        x_axis_label="x",
        y_axis_label="y",
        width=400,
        height=350
    )

    p_test.circle(
        test_df["x"],
        test_df["y"],
        size=6,
        color="green",
        alpha=0.7,
        legend_label="Test Data"
    )
    p_test.legend.location = "top_left"

    # ---------- 3. Mapped test data ----------
    p_mapped = figure(
        title="Mapped Test Data",
        x_axis_label="x",
        y_axis_label="y",
        width=400,
        height=350
    )

    colour_palette = ["red", "blue", "orange", "purple", "brown", "olive"]

    if "ideal_func" not in mapped_df.columns:
        raise KeyError(
            "mapped_df must have a column named 'ideal_func' "
            "(e.g. y24, y40, y13, ...)."
        )

    legend_items_mapped = []

    for i, ideal_col in enumerate(sorted(mapped_df["ideal_func"].unique())):
        sub = mapped_df[mapped_df["ideal_func"] == ideal_col]
        color = colour_palette[i % len(colour_palette)]

        r = p_mapped.circle(
            sub["x"],
            sub["y"],
            size=6,
            color=color,
            alpha=0.8
        )
        legend_items_mapped.append((ideal_col, [r]))

    legend_mapped = Legend(items=legend_items_mapped, location="top_left")
    p_mapped.add_layout(legend_mapped, "right")
    p_mapped.legend.click_policy = "hide"

    layout = row(p_train, p_test, p_mapped)
    show(layout)
