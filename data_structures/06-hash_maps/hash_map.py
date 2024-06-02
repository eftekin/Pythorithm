class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        # If the array index is empty, assign the key-value pair
        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        # If the key already exists, update the value
        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # Collision handling with linear probing
        number_collisions = 1

        while current_array_value[0] != key:
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            # If the new array index is empty, assign the key-value pair
            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            # If the key already exists, update the value
            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        # If the array index is empty, return None
        if possible_return_value is None:
            return None

        # If the key is found, return the value
        if possible_return_value[0] == key:
            return possible_return_value[1]

        # Collision handling with linear probing
        retrieval_collisions = 1

        while possible_return_value[0] != key:
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            # If the new array index is empty, return None
            if possible_return_value is None:
                return None

            # If the key is found, return the value
            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

        return


# Test code
hash_map = HashMap(15)
hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gabbro"))  # Output: igneous
print(hash_map.retrieve("sandstone"))  # Output: sedimentary
print(hash_map.retrieve("gneiss"))  # Output: metamorphic
