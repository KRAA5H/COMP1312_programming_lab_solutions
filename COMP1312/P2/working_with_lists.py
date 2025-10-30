# Complete the definition for copy_doves
def copy_doves(src_list: list[str], dest_list: list[str]) -> None:
    for i in src_list:
        if i.endswith("Dove"):
            dest_list.append(i) 

# Complete the definition of function extract_doves_and_pigeons
def extract_doves_and_pigeons(src_list: list[str]) -> list[str]:
    return [bird for bird in src_list if bird.endswith("Dove") or bird.endswith("Pigeon")]