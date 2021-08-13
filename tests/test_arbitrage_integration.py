from mev_inspect.classifier_specs import CLASSIFIER_SPECS
from mev_inspect.trace_classifier import TraceClassifier
from mev_inspect.arbitrage import get_arbitrages
from mev_inspect.swaps import get_swaps

from .utils import load_test_block


def test_arbitrage_real_block():
    block = load_test_block(12914994)

    trace_clasifier = TraceClassifier(CLASSIFIER_SPECS)
    classified_traces = trace_clasifier.classify(block.traces)

    swaps = get_swaps(classified_traces)
    arbitrages = get_arbitrages(swaps)

    assert len(arbitrages) == 1

    arbitrage = arbitrages[0]

    assert len(arbitrage.swaps) == 3
