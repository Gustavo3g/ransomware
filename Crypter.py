def change_files(filename, cryptoFn, block_size=16):

    with open(filename, 'r+b') as _file:
        raw_value = _file.read(block_size)
        while raw_value:
            cipher_value = cryptoFn(raw_value)
            # compara o tamanho do bloco cifrado e plano (plain text)
            if len(raw_value) != len(cipher_value):
                raise ValueError(f'O valor cifrado {len(cipher_value)} tem valor doferente do valor plano {len(raw_value)}')

            _file.seek(-len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)