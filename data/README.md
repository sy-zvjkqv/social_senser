# data directory
```
├── mobile/                                 <-モバイル空間統計データ
│   ├──original/                            <-届いたまんまでおいてある
│   ├──Tokyostaion_2021/                    <-2021年1月1日から2022年7月31日までの東京駅人流データ
|        ├──numpy_array/
|           ├──Tokyostation2021.npy         <-'Tokyostation_2021to2022'の人流データを東京駅でかつ2021年のもので絞りnp_aarrayで保存したもの day-hourの２次元
|        ├──Tokyostation_2021to2022.csv     <-'../original/01_1_東京駅を含むエリアの１年間のデータ_総数.csv'と同じ
|
├── twitter/                                <-ツイッタースクレイピングデータ
│    ├── Tokyostation_2021/ 
|            ├──numpy_array/
|            |   ├──Tokyostation_3zi_2021.npy<-'Tokyostation_3zi_2021.csv'の人流データを東京駅で絞りかつnp_aarrayで保存したもの day-hourの２次元
|            ├──Tokyostation_3zi_2021.csv    <-2021年1月1日から12月31日までの東京駅位置情報付きデータ クエリ: 'lang:ja bounding_box:[139.7625 35.675 139.775 35.6833]'
```
Training data should be placed under this directory.
