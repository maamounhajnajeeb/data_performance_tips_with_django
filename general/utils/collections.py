def deep_update(base_dict, update_with):
    # Iterate over each item in the new dict
    for k, v in update_with.items():

        # If the value is a dict
        if isinstance (v, dict):
            base_dict_value = base_dict.get(k)

            # If the original value is also a dict then run it through this same function
            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, v)
            # If the original value is NOT a dict then just set the new value
            else:
                base_dict[k] = v
        # If the new value is NOT a dict
        else:
            base_dict[k] = v

    return base_dict
