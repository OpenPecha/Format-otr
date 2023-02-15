from format_otr.export_txt import get_txt
from pathlib import Path

input_path = './tests/data/test_1.otr'
expected_out = Path('./tests/data/expected/txt/test_1.txt').read_text(encoding='utf8')


def test_get_txt():
    output_txt = get_txt(input_path)
    assert output_txt.strip() == expected_out.strip()

if __name__ == '__main__':
    test_get_txt()