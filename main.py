from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)
app

# BUAT MENJALANKAN APLIKASI, JANGAN DIHAPUS
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)