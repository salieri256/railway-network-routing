# スクリプト集

## 路線ファイルをマージする

```bash
python3 merge.py <マージする路線ファイル> <出力先> <名前空間>
```

JR 西日本の全路線ファイルをひとつのファイルに集約する例:

```bash
python3 merge.py ../jr-west/lines/!(all)/topology.clab.yml ../jr-west/lines/all/topology.clab.yml jr-west
```
