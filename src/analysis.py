class BOQAnalyzer:
    def __init__(self ):
        self.default_unit = "mm"
        self.units = {
            "millimeter": {
                "scale_factor": 1,
                      },
            "meters": {
                "scale_factor": 0.001, 
                      },
            "feet": {
                "scale_factor": 0.00302, 
                      },

                      }
        self.results = []

    def _area_in_m_square(self, width:int, height:int):
        if self.default_unit != "mm":
            prefered_unit = self.default_unit
            unit_to_mm_scale_factor = self.units[prefered_unit]['scale_factor']
            width_in_mm = width * unit_to_mm_scale_factor
            height_in_mm = height * unit_to_mm_scale_factor

        else:
            width_in_m = width / 1000
            height_in_m = height / 1000
        area_in_m_square = width_in_m * height_in_m

        return area_in_m_square

    def block_per_area(self, width:int, height:int, wallname:str):
        area = self._area_in_m_square(width, height) 
        block = round(area * 10)
        self.results.append((wallname, block))

    def get_block_sum(self):
        return 0, 0 if len(self.results) == 0 else self._get_block_sum()

    def _get_block_sum(self):
        name_list = []
        blocks_list = []

        for result in self.results:
            name, blocks = result
            name_list.append(name)
            blocks_list.append(blocks)

        total_faces = len(name_list)
        block_sum = sum(blocks_list)

        return total_faces, block_sum

