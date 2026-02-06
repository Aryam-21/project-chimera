"""
Failing tests for the Trend Fetching capability.

These tests define the expected data contract.
No implementation exists yet — failure is expected.
"""
def test_trend_fetcher_output_structure():
    """
    The trend fetcher must return a dictionary
    matching the documented API contract.
    """

    # Placeholder for future implementation
    # from skills.skill_fetch_trends import fetch_trends
    # result = fetch_trends(...)
    result = None #Intentional placeholder
    assert  isinstance(result, dict), "Trend fetcher must return a dict"
    assert 'trends' is result, 'Result must contain "trends" key'
    assert isinstance(result['trends'], list), "'trends' must be a list"
    for trend in result['trends']:
        assert 'topic' in trend
        assert 'velocity_score' in trend
        assert 'sample_posts' in trend
        assert isinstance(trend['topic'], str)
        assert isinstance(trend['velocity_score'], (int, float))
        assert isinstance(trend['sample_posts'], list)
    assert "fetched_at" in result, "Result must include timestamp"