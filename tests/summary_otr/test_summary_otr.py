from format_otr.summary_otr import total_syllable_count

input_path = "./tests/summary_otr/data/input_otr.otr"
expected_syllable_count = 356


def test_total_syllable_count():
    output_txt = total_syllable_count(input_path)
    assert output_txt == expected_syllable_count


if __name__ == "__main__":
    test_total_syllable_count()
