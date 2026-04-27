# スクリプト集

## 路線ファイルを整形する

```bash
python3 format.py <整形する路線ファイル> <出力先>
```

JR 西日本の大阪環状線の路線ファイルを整形する例:

```bash
python3 format.py ../jr-west/lines/osaka-loop-line/topology.clab.yml ../jr-west/lines/osaka-loop-line/topology.clab.yml
```

## 路線ファイルをマージする

```bash
python3 merge.py <マージする路線ファイル> <出力先> <名前空間>
```

JR 西日本の全路線ファイルをひとつのファイルに集約する例:

```bash
python3 merge.py ../jr-west/lines/!(all)/topology.clab.yml ../jr-west/lines/all/topology.clab.yml jr-west
```
