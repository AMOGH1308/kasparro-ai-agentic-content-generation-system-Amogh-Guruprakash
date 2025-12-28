from logic_blocks.parsing import parse_product_data

class InputParserAgent:
    def run(self, raw_data):
        return parse_product_data(raw_data)
