#!/usr/bin/env python3
import gzip, re, sys
from pathlib import Path
for arg in sys.argv[1:]:
    p=Path(arg); raw=p.read_bytes(); text=(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw).decode('utf-8','replace')
    print(f'## {p.name}')
    for value in re.findall(r'<dia:string>#(.*?)#</dia:string>', text):
        if value.strip(): print(value)
