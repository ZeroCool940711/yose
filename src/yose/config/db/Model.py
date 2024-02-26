from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import (
    BOOLEAN,
    DATETIME,
    ID,
    IDLIST,
    KEYWORD,
    NGRAM,
    NGRAMWORDS,
    NUMERIC,
    STORED,
    TEXT,
    SchemaClass,
)

analyzer = StemmingAnalyzer(stoplist=None)


class Options(SchemaClass):
    id = ID(stored=True, unique=True)
    app_title = TEXT(stored=True)
    theme_mode = TEXT(stored=True)
    language = TEXT(stored=True)
    show_nav_bar_updates = BOOLEAN(stored=True)
    show_nav_bar_history = BOOLEAN(stored=True)
    show_nav_bar_labels = BOOLEAN(stored=True)
    expand_search_filters = BOOLEAN(stored=True)
    recommendations_in_overflow_menu = BOOLEAN(stored=True)
    merge_in_overflow_menu = BOOLEAN(stored=True)
    per_category_sorting = BOOLEAN(stored=True)
    automatic_updates_interval = NUMERIC(stored=True)
    automatically_refresh_metadata = BOOLEAN(stored=True)
    show_unread_count_in_update_button = BOOLEAN(stored=True)


class IndexItems(SchemaClass):
    author = TEXT(analyzer=analyzer, stored=True, sortable=True)
    author_email = TEXT(analyzer=analyzer, stored=True, sortable=True)
    author_link = TEXT(analyzer=analyzer, stored=True, sortable=True)
    category = TEXT(analyzer=analyzer, stored=True, sortable=True)
    comment_count = NUMERIC(stored=True, default=0)
    comments = TEXT(analyzer=analyzer, stored=True, sortable=True)
    content_type = TEXT(analyzer=analyzer, stored=True, sortable=True)
    description = TEXT(analyzer=analyzer, stored=True, sortable=True)
    download_count = NUMERIC(stored=True, default=0)
    duration = NUMERIC(stored=True, default=0)
    ext = TEXT(analyzer=analyzer, stored=True, sortable=True)
    file = TEXT(analyzer=analyzer, stored=True, sortable=True)
    guid = ID(stored=True, unique=True)
    hashtags = TEXT(analyzer=analyzer, stored=True, sortable=True)
    host = TEXT(analyzer=analyzer, stored=True, sortable=True)
    image = TEXT(analyzer=analyzer, stored=True, sortable=True)
    keywords = TEXT(analyzer=analyzer, stored=True, sortable=True)
    language = TEXT(analyzer=analyzer, stored=True, sortable=True)
    likes = NUMERIC(stored=True, default=0, sortable=True)
    link = TEXT(analyzer=analyzer, stored=True, sortable=True)
    location = TEXT(analyzer=analyzer, stored=True, sortable=True)
    path = TEXT(analyzer=analyzer, stored=True, sortable=True)
    protocol = TEXT(analyzer=analyzer, stored=True, sortable=True)
    pubDate = DATETIME(stored=True, sortable=True)
    rating = NUMERIC(stored=True)
    rating_count = NUMERIC(stored=True)
    sentiment = TEXT(analyzer=analyzer, stored=True, sortable=True)
    sentiment_score = NUMERIC(stored=True, sortable=True, default=0)
    shares = NUMERIC(stored=True, default=0, sortable=True)
    size = NUMERIC(stored=True, sortable=True, default=0)
    sizename = TEXT(analyzer=analyzer, stored=True, sortable=True)
    source = TEXT(analyzer=analyzer, stored=True, sortable=True)
    tags = KEYWORD(analyzer=analyzer, stored=True, sortable=True, commas=True)
    title = TEXT(analyzer=analyzer, stored=True, sortable=True)
    views = NUMERIC(stored=True, default=0, sortable=True)
    year = NUMERIC(stored=True, sortable=True)
    month = NUMERIC(stored=True, sortable=True)
    day = NUMERIC(stored=True, sortable=True)
    hour = NUMERIC(stored=True, sortable=True)
    minute = NUMERIC(stored=True, sortable=True)
    second = NUMERIC(stored=True, sortable=True)
    is_featured = BOOLEAN(stored=True)
    is_trending = BOOLEAN(stored=True)
    is_new = BOOLEAN(stored=True)
    is_popular = BOOLEAN(stored=True)
    is_verified = BOOLEAN(stored=True)
    is_active = BOOLEAN(stored=True)
    is_deleted = BOOLEAN(stored=True)
    created_at = DATETIME(stored=True, sortable=True)
    updated_at = DATETIME(stored=True, sortable=True)
    deleted_at = DATETIME(stored=True, sortable=True)
    last_used = DATETIME(stored=True, sortable=True)
