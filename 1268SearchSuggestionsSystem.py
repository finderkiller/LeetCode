class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        pre_output = products
        for idx in range(len(searchWord)):
            prefix = searchWord[:idx+1]
            output = []
            for product in pre_output:
                if product.find(prefix) != 0:
                    continue
                output.append(product)
            pre_output = output
            result.append(output[:3])
        return result