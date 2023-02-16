from format_otr.format_otr import get_format_otr
from pathlib import Path

input_path = "./tests/format_otr/data/input_otr.otr"
expected_out = Path("./tests/format_otr/data/expected_otr.otr").read_text(
    encoding="utf8"
)


def test_get_format_txt():
    output_otr = get_format_otr(input_path)
    assert expected_out.strip() == output_otr.strip()


if __name__ == "__main__":
    test_get_format_txt()
