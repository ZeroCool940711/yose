import asyncio
import sys
from typing import List

import requests
from loguru import logger
from nicegui import app, color, events, icon, ui

from yose.utils import (
    add_document,
    first_run,
    get_all_documents,
    get_options,
    search_documents,
    set_icon,
)

app.native.window_args["resizable"] = True


# def startup():
#     loop = asyncio.get_running_loop()
#     loop.set_debug(True)
#     loop.slow_callback_duration = 0.1


# app.on_startup(startup)

ui.query(".nicegui-content").classes("p-0")


@ui.page("/search")
def search_page():
    ui.label("Search page not implemented yet.")


@ui.page("/SystemStatus")
def system_status():
    ui.label("System Status page not implemented yet.")


@ui.page("/P2PNetwork")
def p2p_network():
    ui.label("P2P Network page not implemented yet.")


@ui.page("/IndexBrowser")
def index_browser():
    ui.label("Index Browser page not implemented yet.")


@ui.page("/NetworkAccess")
def network_access():
    ui.label("Network Access page not implemented yet.")


@ui.page("/CrawlerMonitor")
def crawler_monitor():
    ui.label("Crawler Monitor page not implemented yet.")


@ui.page("/AdvancedCrawler")
def advanced_crawler():
    ui.label("Advanced Crawler page not implemented yet.")


@ui.page("/IndexExportImport")
def index_export_import():
    ui.label("Index Export/Import page not implemented yet.")


@ui.page("/ContentSemantic")
def content_semantic():
    ui.label("Content Semantic page not implemented yet.")


@ui.page("/TargetAnalysis")
def target_analysis():
    ui.label("Target Analysis page not implemented yet.")


@ui.page("/IndexAdministration")
def index_administration():
    ui.label("Index Administration page not implemented yet.")


@ui.page("/SystemAdministration")
def system_administration():
    ui.label("System Administration page not implemented yet.")


@ui.page("/FilterBlacklists")
def filter_blacklists():
    ui.label("Filter & Blacklists page not implemented yet.")


@ui.page("/ProcessScheduler")
def process_scheduler():
    ui.label("Process Scheduler page not implemented yet.")


@ui.page("/GeneralSettings")
def general_settings():
    ui.label("General Settings page not implemented yet.")


@ui.page("/ThemeSettings")
def theme_settings():
    ui.label("Theme Settings page not implemented yet.")


@ui.page("/RankingHeuristics")
def ranking_heuristics():
    ui.label("Ranking and Heuristics page not implemented yet.")


@ui.page("/UseCase")
def use_case():
    ui.label("Use Case & Account page not implemented yet.")


@ui.page("/WebCrawler")
def web_crawler():
    ui.label("Load Web Pages, Crawler page not implemented yet.")


@ui.page("/RAMDiskUsage")
def ram_disk_usage():
    ui.label("RAM/Disk Usage & Updates page not implemented yet.")


@ui.page("/admin")
def admin_panel():
    SideBar()


def get_or_create_search_index(query, max_results=50, page=0):
    results = requests.get(
        f"http://localhost:8090/yacysearch.json?query={query}&Enter=&auth=&verify=ifexist&contentdom=image&nav=location%2Chosts%2Cauthors%2Cnamespace%2Ctopics%2Cfiletype%2Cprotocol%2Clanguage&startRecord={page * max_results}&indexof=off&meanCount=5&resource=global&prefermaskfilter=&maximumRecords={max_results}&timezoneOffset=420"
    ).json()["channels"][0]["items"]

    # async for result in results:
    #     await add_document(result)

    return results


@ui.page("/search/web")
def web_search_page(query: str = ""):
    ui.label("Web search page not implemented yet.")


class Lightbox:
    """A thumbnail gallery where each image can be clicked to enlarge.
    Inspired by https://lokeshdhakar.com/projects/lightbox2/.
    """

    def __init__(self) -> None:
        with ui.dialog().props("maximized").classes("bg-transparent") as self.dialog:
            ui.keyboard(self._handle_key)
            self.large_image = ui.image().props("no-spinner fit=scale-down")
        self.image_list: List[str] = []

    def add_image(self, thumb_url: str, orig_url: str) -> ui.image:
        """Place a thumbnail image in the UI and make it clickable to enlarge."""
        self.image_list.append(orig_url)
        with ui.button(on_click=lambda: self._open(orig_url)).props(
            "flat dense square"
        ):
            return ui.image(thumb_url)

    def _handle_key(self, event_args: events.KeyEventArguments) -> None:
        if not event_args.action.keydown:
            return
        if event_args.key.escape:
            self.dialog.close()
        image_index = self.image_list.index(self.large_image.source)
        if event_args.key.arrow_left and image_index > 0:
            self._open(self.image_list[image_index - 1])
        if event_args.key.arrow_right and image_index < len(self.image_list) - 1:
            self._open(self.image_list[image_index + 1])

    def _open(self, url: str) -> None:
        self.large_image.set_source(url)
        self.dialog.open()


@ui.page("/search/images")
def image_search_page(query: str = "* /date", page: int = 0, max_results: int = 50):
    SearchFilters()
    lightbox = Lightbox()

    def infinite_scroll(
        query: str = "* /date", page: int = 0, max_results: int = max_results
    ):
        with results_grid:
            for result in get_or_create_search_index(query, max_results, page):
                with ui.card():
                    lightbox.add_image(
                        thumb_url=f"{result['image']}",
                        orig_url=f"{result['image']}",
                    ).classes("w-[300px] h-[200px]")
                    ui.link(result["title"], result["image"])
                    ui.label(result["host"])

        #logger.debug(f"page: {page + 1}")

        load_more = ui.button(
            "Load More",
            on_click=lambda e: [
                infinite_scroll(query, page + 1, max_results),
                load_more.set_visibility(False),
            ],
        ).style("align-self: center; width: 100%;")

    with ui.column().style("width: 100%; height: 100%; padding: 0; margin: 0;"):
        with ui.page_sticky("top").style(
            "width: 100%; gap: 1px; padding: 0; margin-left: 2%; z-index: 1000 !important;"
        ):
            with ui.row():
                ui.label(options["app_title"]).style(
                    "font-size: 2.5em; font-weight: bold; text-shadow: 2px 2px 2px #000;"
                ).on("click", lambda e: ui.navigate.to("/")).tailwind.font_style(
                    "italic"
                ).font_family("serif").align_self("start").drop_shadow(
                    "lg"
                ).backdrop_blur("lg").opacity("0.2").align_self("start")

                for _ in range(5):
                    ui.space()

                search_field = (
                    ui.input(label="Search the web...", value=query)
                    .style(
                        "width: 60%; bg-opacity: 0.2; drop-shadow: lg; backdrop-blur: lg; text-shadow: 2px 2px 2px #000; align-self: end;"
                    )
                    .props("autofocus outlined rounded bg-opacity-20")
                    .classes("elevation-4")
                ).on(
                    "keydown.enter",
                    lambda e: ui.navigate.to(
                        f"/search/images?query={search_field.value}"
                    ),
                )

                ui.button(
                    "Administration",
                    icon=icon.SETTINGS,
                    color=color.TRANSPARENT,
                    on_click=lambda e: ui.navigate.to("/admin"),
                ).style("text-shadow: 2px 2px 2px #000;").tailwind.align_self(
                    "end"
                ).drop_shadow("lg").backdrop_blur("lg").opacity("0.2")

                with ui.button(icon=icon.MENU, color=color.TRANSPARENT).style(
                    "align-self: end; bg-opacity: 0.2; drop-shadow: lg; backdrop-blur: lg; text-shadow: 2px 2px 2px #000;"
                ):
                    with ui.menu().style(
                        "bg-opacity: 0.2; drop-shadow: lg; backdrop-blur: lg"
                    ):
                        ui.menu_item(
                            "Settings", on_click=lambda e: ui.navigate.to("/settings")
                        )

                for _ in range(50):
                    ui.space()

            with ui.row():
                ui.button(
                    "Web",
                    icon=icon.WEB,
                    color=color.TRANSPARENT,
                    on_click=lambda e: ui.navigate.to("/search/web"),
                ).style("text-shadow: 2px 2px 2px #000;").tailwind.align_self(
                    "end"
                ).drop_shadow("lg").backdrop_blur("lg").opacity("0.2")
                ui.button(
                    "Images",
                    icon=icon.IMAGE,
                    color=color.TRANSPARENT,
                    on_click=lambda e: ui.navigate.to("/search/images"),
                ).style("text-shadow: 2px 2px 2px #000;").tailwind.align_self(
                    "end"
                ).drop_shadow("lg").backdrop_blur("lg").opacity("0.2")
                ui.button(
                    "Videos",
                    icon=icon.PLAY_CIRCLE,
                    color=color.TRANSPARENT,
                    on_click=lambda e: ui.navigate.to("/search/videos"),
                ).style("text-shadow: 2px 2px 2px #000;").tailwind.align_self(
                    "end"
                ).drop_shadow("lg").backdrop_blur("lg").opacity("0.2")
                ui.button(
                    "News",
                    icon=icon.NEWS,
                    color=color.TRANSPARENT,
                    on_click=lambda e: ui.navigate.to("/search/news"),
                ).style("text-shadow: 2px 2px 2px #000;").tailwind.align_self(
                    "end"
                ).drop_shadow("lg").backdrop_blur("lg").opacity("0.2")

        with ui.grid(columns=6, rows=6).style(
            "object-fit: scale-down; justify-content: center; margin-top: 5%; "
        ).props("scrollable").classes("mx-auto") as results_grid:
            for result in get_or_create_search_index(query, max_results, page):
                # logger.debug(result)

                with ui.card():
                    lightbox.add_image(
                        thumb_url=f"{result['image']}",
                        orig_url=f"{result['image']}",
                    ).classes("w-[300px] h-[200px]")
                    ui.link(result["title"], result["image"])
                    ui.label(result["host"])

        load_more = ui.button(
            "Load More",
            on_click=lambda e: [
                infinite_scroll(query, page + 1, max_results),
                load_more.set_visibility(False),
            ],
        ).style("align-self: center; width: 100%;")


@ui.page("/search/videos")
def search_videos(query: str = ""):
    ui.label("Videos search page not implemented yet.")


@ui.page("/search/news")
def search_news(query: str = ""):
    ui.label("News search page not implemented yet.")


class SearchFilters(ui.element):
    def __init__(self, *args, **kwargs):
        self.build()

    def build(self):
        self.menu_width = "width: 100%"

        with ui.left_drawer(
            value=False,
            elevated=True,
            bordered=True,
        ).style(
            "align-items: center; gap: 2px; padding: 0; margin: 0; width: 100%;"
        ) as self.left_drawer:
            ui.label("Search Filters").style("font-size: 2rem; align-self: center; ")
            ui.separator().style(self.menu_width)

            # ui.label("First Steps").style(
            #     ui.Style(text_align="center", width="100%", bgcolor=color.PRIMARY)
            # )

            # ui.button(
            #     "Use Case & Account",
            #     color=color.SLATE700,
            #     on_click=lambda e: ui.navigate.to("/UseCase"),
            # ).style(self.menu_width)

            # ui.button(
            #     "Load Web Pages, Crawler",
            #     color=color.SLATE700,
            #     on_click=lambda e: ui.navigate.to("/WebCrawler"),
            # ).style(self.menu_width)

        ui.button(
            on_click=lambda: self.left_drawer.toggle(), icon=icon.FILTER_LIST
        ).tailwind.position("fixed").z_index("50")


class SideBar(ui.element):
    def __init__(self, *args, **kwargs):
        self.build()

    def build(self):
        self.menu_width = "width: 100%"

        with ui.left_drawer(
            elevated=True,
            bordered=True,
        ).style(
            "align-items: center; gap: 2px; padding: 0; margin: 0; width: 100%;"
        ) as self.left_drawer:
            ui.label("Admin Panel").style("font-size: 2rem; align-self: center; ").on(
                "click", lambda e: ui.navigate.to("/")
            )
            ui.separator().style(self.menu_width)

            ui.label("First Steps").style(
                ui.Style(text_align="center", width="100%", bgcolor=color.PRIMARY)
            )

            ui.button(
                "Use Case & Account",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/UseCase"),
            ).style(self.menu_width)

            ui.button(
                "Load Web Pages, Crawler",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/WebCrawler"),
            ).style(self.menu_width)

            ui.button(
                "RAM/Disk Usage & Updates",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/RAMDiskUsage"),
            ).style(self.menu_width)
            ui.separator().style(self.menu_width)

            ui.label("Monitoring").style(
                ui.Style(text_align="center", width="100%", bgcolor=color.PRIMARY)
            )
            ui.button(
                "System Status",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/SystemStatus"),
            ).style(self.menu_width)

            ui.button(
                "Peer-to-Peer Network",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/P2PNetwork"),
            ).style(self.menu_width)

            ui.button(
                "Index Browser",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/IndexBrowser"),
            ).style(self.menu_width)

            ui.button(
                "Network Access",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/NetworkAccess"),
            ).style(self.menu_width)

            ui.button(
                "Crawler Monitor",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/CrawlerMonitor"),
            ).style(self.menu_width)

            ui.separator().style(self.menu_width)

            ui.label("Production").style(
                ui.Style(text_align="center", width="100%", bgcolor=color.PRIMARY)
            )
            ui.button(
                "Advanced Crawler",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/AdvancedCrawler"),
            ).style(self.menu_width)

            ui.button(
                "Index Export/Import",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/IndexExportImport"),
            ).style(self.menu_width)

            ui.button(
                "Content Semantic",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/ContentSemantic"),
            ).style(self.menu_width)

            ui.button(
                "Target Analysis",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/TargetAnalysis"),
            ).style(self.menu_width)

            ui.separator().style(self.menu_width)

            ui.label("Administration").style(
                ui.Style(text_align="center", width="100%", bgcolor=color.PRIMARY)
            )
            ui.button(
                "Index Administration",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/IndexAdministration"),
            ).style(self.menu_width)

            ui.button(
                "System Administration",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/SystemAdministration"),
            ).style(self.menu_width)

            ui.button(
                "Filter & Blacklists",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/FilterBlacklists"),
            ).style(self.menu_width)

            ui.button(
                "Process Scheduler",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/ProcessScheduler"),
            ).style(self.menu_width)

            ui.separator().style(self.menu_width)

            ui.label("Search Portal Integration").style(
                ui.Style(text_align="center", width="100%", bgcolor=color.PRIMARY)
            )
            ui.button(
                "General Settings",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/GeneralSettings"),
            ).style(self.menu_width)

            ui.button(
                "Theme Settings",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/ThemeSettings"),
            ).style(self.menu_width)

            ui.button(
                "Ranking and Heuristics",
                color=color.SLATE700,
                on_click=lambda e: ui.navigate.to("/RankingHeuristics"),
            ).style(self.menu_width)

        ui.button(on_click=lambda: self.left_drawer.toggle(), icon=icon.MENU)


@ui.page("/", title="Yose")
def home_page():
    ui.image("https://picsum.photos/1900/1000").style(
        "position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    )

    # with background_image:
    with ui.page_sticky("top").style(
        "width: 100%; gap: 1px; padding: 0; margin-left: 2% ;"
    ):
        with ui.row():
            ui.label(options["app_title"]).style(
                "font-size: 2.5em; font-weight: bold; text-shadow: 2px 2px 2px #000;"
            ).on("click", lambda e: ui.navigate.to("/")).tailwind.font_style(
                "italic"
            ).font_family("serif").align_self("start").drop_shadow("lg").backdrop_blur(
                "lg"
            ).opacity("0.2")

            ui.button(
                "Web",
                icon=icon.WEB,
                color=color.TRANSPARENT,
                on_click=lambda e: ui.navigate.to("/search/web"),
            ).style("text-shadow: 2px 2px 2px #000;").tailwind.align_self(
                "end"
            ).drop_shadow("lg").backdrop_blur("lg").opacity("0.2")
            ui.button(
                "Images",
                icon=icon.IMAGE,
                color=color.TRANSPARENT,
                on_click=lambda e: ui.navigate.to("/search/images"),
            ).style("text-shadow: 2px 2px 2px #000;").tailwind.align_self(
                "end"
            ).drop_shadow("lg").backdrop_blur("lg").opacity("0.2")
            ui.button(
                "Videos",
                icon=icon.PLAY_CIRCLE,
                color=color.TRANSPARENT,
                on_click=lambda e: ui.navigate.to("/search/videos"),
            ).style("text-shadow: 2px 2px 2px #000;").tailwind.align_self(
                "end"
            ).drop_shadow("lg").backdrop_blur("lg").opacity("0.2")
            ui.button(
                "News",
                icon=icon.NEWS,
                color=color.TRANSPARENT,
                on_click=lambda e: ui.navigate.to("/search/news"),
            ).style("text-shadow: 2px 2px 2px #000;").tailwind.align_self(
                "end"
            ).drop_shadow("lg").backdrop_blur("lg").opacity("0.2")

            for _ in range(30):
                ui.space()

            ui.button(
                "Administration",
                icon=icon.SETTINGS,
                color=color.TRANSPARENT,
                on_click=lambda e: ui.navigate.to("/admin"),
            ).style("text-shadow: 2px 2px 2px #000;").tailwind.align_self(
                "end"
            ).drop_shadow("lg").backdrop_blur("lg").opacity("0.2")

            with ui.button(icon=icon.MENU, color=color.TRANSPARENT).style(
                "align-self: end; bg-opacity: 0.2; drop-shadow: lg; backdrop-blur: lg; text-shadow: 2px 2px 2px #000;"
            ):
                with ui.menu().style(
                    "bg-opacity: 0.2; drop-shadow: lg; backdrop-blur: lg"
                ):
                    ui.menu_item(
                        "Settings", on_click=lambda e: ui.navigate.to("/settings")
                    )

    with ui.row().style(
        "height: 80%; width: 100%; padding: 25%; justify-content: center; align-items: center"
    ).props("item-aligned"):
        # create a search field which is initially focused and leaves space at the top
        search_field = (
            ui.input(label="Search the web...")
            .style(
                "width: 60%; bg-opacity: 0.2; drop-shadow: lg; backdrop-blur: lg; text-shadow: 2px 2px 2px #000;"
            )
            .props("autofocus outlined rounded item-aligned bg-opacity-20")
            .classes("elevation-4")
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
        # viewport="width=device-width,initial-scale=1,shrink-to-fit=no",
        reload=True,
        native=True,
        # window_size=(430, 660),
        # on_air=True,
    )
