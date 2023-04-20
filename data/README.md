# data directory
```
├── mobile/                                 <-モバイル空間統計データ
|   |──Kyoto/                                <京都各エリアのデータ
│   ├──original/                            <-届いたまんまでおいてある
│   ├──Tokyostaion_2021/                    <-2021年1月1日から2022年7月31日までの東京駅人流データ
|
├── twitter/                                <-ツイッタースクレイピングデータ
│    ├── Tokyostation_2021/ 
|    |        |──Tokyostation_3zi_2021.npy<-'Tokyostation_3zi_2021.csv'の人流データを東京駅で絞りかつnp_aarrayで保存したもの day-hourの２次元
|    |        ├──Tokyostation_3zi_2021.csv    <-2021年1月1日から12月31日までの東京駅位置情報付きデータ 地域メッシュコード: 5339-46-11 クエリ: 'lang:ja bounding_box:[139.7625 35.675 139.775 35.6833]'
|    |        ├──processed_Tokyostation_3zi_2021.csv <-Tokyostation_3zi_2021.csvに前処理で時間の列をついかしたもの
|    |-Kyoto      
|        |── nouse_Kyotostation_2021/ 
         |       ├──Kyotostation_3zi_2021.csv        <-2021年1月1日から12月31日までの京都駅位置情報付きデータ　地域メッシュコード: 5235-36-80 クエリ:'lang:ja bounding_box:[135.75 34.983333333333 135.7625 34.991666666667]'
         |       ├──Kyotostation_3zi_2021.npy  
         |── nouse_Kyotostation_2022/ 
                ├──Kyotostation_3zi_2022.csv        <-2022年1月1日から12月31日までの京都駅位置情報付きデータ　地域メッシュコード: 5235-36-80 クエリ:'lang:ja bounding_box:[135.75 34.983333333333 135.7625 34.991666666667]'
         |      ├──Kyotostation_3zi_2022.npy  
         |── npy/                               <-npy形式で保存したツイート数遷移 ./Kyoto　内のcsvファイルから
         |── proceeed/                           <- ./Kyoto　内のcsvファイルから作成　月, 日, 時間の列を追加
```
