//
// esri map
//

require([
    "esri/Map",
    "esri/views/MapView",
    "esri/layers/FeatureLayer",
    "esri/widgets/Legend",
], function (Map, MapView, FeatureLayer, Legend) {
    var activeWidget = null;
    const FireLayer = new FeatureLayer({
        url:
            "https://services9.arcgis.com/lYhg5zlSTPlHaacE/arcgis/rest/services/FireBooth/FeatureServer",
        title: "杭州消防站分布",
        popupTemplate: {
            // autocast as esri/PopupTemplate
            title: "{name}",
            content: [
                {
                    // It is also possible to set the fieldInfos outside of the content
                    // directly in the popupTemplate. If no fieldInfos is specifically set
                    // in the content, it defaults to whatever may be set within the popupTemplate.
                    type: "fields",
                    fieldInfos: [
                        {
                            fieldName: "address",
                            label: "地址",
                            format: {
                                place: "未知"
                            }
                        },
                        {
                            fieldName: "tel",
                            label: "联系方式",
                            format: {
                                places: "暂无"
                            }
                        },
                        {
                            fieldName: "adname",
                            label: "所属地市区县"
                        }]
                }
            ]
        }
    });

    var map = new Map({
        basemap: "topo-vector",
        layers: [FireLayer]
    });

    var view = new MapView({
        container: "map-default",
        map: map,
        center: [120.100, 30.20],
        zoom: 9
    });

    /* const legend = new Legend({
      view: view,
      style: {
        type: "card",
        layout: "side-by-side"
      }
    });

    view.ui.add(legend, "top-right"); */

});