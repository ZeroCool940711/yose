import sys

from loguru import logger
from nicegui import Client, app, color, icon, ui

from yose.utils import first_run, get_options, set_icon

app.native.window_args["resizable"] = True

ui.query(".nicegui-content").classes("p-0")


@ui.page("/search")
def search_page():
    with ui.row().style("height: 100%; width: 100%; gap: 0; "):
        with ui.column().style("width: 30%; height: 100%; align-self: start;"):
            ui.space()

        # ui.splitter()

        with ui.column().style("width: 70%; height: 100%;"):
            # create a search field which is initially focused and leaves space at the top
            search_field = (
                ui.input()
                .style("width: 40%;")
                .props("autofocus outlined rounded item-aligned")
            )
            with ui.row().style("justify-content: start;"):
                ui.button("Web", icon=icon.WEB)
                ui.button("Images", icon=icon.IMAGE)
                ui.button("Videos", icon=icon.PLAY_CIRCLE)

            # results = ui.row()


@ui.page("/admin")
def admin_panel():
    ui.label("Admin Panel not implemented yet.")


@ui.page("/", title="Yose")
def index(client: Client):
    ui.image("https://picsum.photos/1900/1000").style(
        "position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    )

    # with background_image:
    with ui.page_sticky("top").style("width: 100%; gap: 1px; padding: 0; "):
        with ui.row().style("opacity: 0.9;"):
            ui.label("Yose").style(
                "font-size: 2.5em; font-weight: bold;"
            ).tailwind.font_family("serif").align_self("start")

            ui.button(
                "Web", icon=icon.WEB, color=color.TRANSPARENT
            ).tailwind.align_self("end").drop_shadow("2xl").backdrop_blur("2xl")
            ui.button(
                "Images", icon=icon.IMAGE, color=color.TRANSPARENT
            ).tailwind.align_self("end").drop_shadow("2xl").backdrop_blur("2xl")
            ui.button(
                "Videos", icon=icon.PLAY_CIRCLE, color=color.TRANSPARENT
            ).tailwind.align_self("end").drop_shadow("2xl").backdrop_blur("2xl")
            ui.button(
                "News", icon=icon.NEWS, color=color.TRANSPARENT
            ).tailwind.align_self("end").drop_shadow("2xl").backdrop_blur("2xl")

            for _ in range(30):
                ui.space()

            ui.button(
                "Administration",
                icon=icon.SETTINGS,
                color=color.TRANSPARENT,
                on_click=lambda e: ui.open("/admin"),
            ).tailwind.align_self("end").drop_shadow("2xl").backdrop_blur("2xl")

    with ui.row().style(
        "height: 80%; width: 100%; padding: 25%; justify-content: center; align-items: center"
    ).props("item-aligned") as search_row:
        # create a search field which is initially focused and leaves space at the top
        search_field = (
            ui.input(label="Search the web...")
            .style("width: 60%;")
            .props("autofocus outlined rounded item-aligned drop-shadow-2xl")
        ).on("keydown.enter", lambda e: print(f"searching...{search_field.value}"))


if __name__ in {"__main__", "__mp_main__"}:
    # we need to first remove the default logger and then add a new one for the levels to work
    logger.remove()
    logger.add(sys.stderr, level="DEBUG")

    first_run()
    set_icon()

    options = get_options()

    ui.run(
        port=5000,
        title=options["app_title"],
        dark=True if options["theme_mode"] == "dark" else False,
        reload=True,
        native=True,
        # window_size=(430, 660),
        # on_air=True,
    )
