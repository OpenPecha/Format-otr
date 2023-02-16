from format_otr.export_otr import get_txt
from pathlib import Path

input_path = "./tests/export_otr/data/input_otr.otr"
expected_out = Path("./tests/export_otr/data/expected_txt.txt").read_text(
    encoding="utf8"
)


def test_get_txt():
    output_txt = get_txt(input_path)
    assert output_txt.strip() == expected_out.strip()


if __name__ == "__main__":
    test_get_txt()
