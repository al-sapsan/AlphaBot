"""Базовый тест импорта пакета."""

def test_package_import():
    """Проверить, что пакет импортируется."""
    import alpha_bot_driver
    assert alpha_bot_driver.__version__ == '0.1.0'
