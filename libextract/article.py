from .metrics import text_length
from .procs import select, rank_with, most_common, histogram
from .xpaths import TEXT_NODES


def parent_length_pairs(results):
    for node, metric in results:
        yield node.getparent(), metric


def build_strategy(count=5):
    return (
        select(TEXT_NODES),
        rank_with(text_length),
        histogram(parent_length_pairs),
        most_common(count)
    )
