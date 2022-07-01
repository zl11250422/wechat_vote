var config = require('../../utils/config.js');

Page({

  /**
   * 初始化装载数据
   */
  onLoad: function (options) {
    var that = this;
    //获取投票主题
    wx.request({
      url: 'http://127.0.0.1:8000/title',
      method: 'GET',
      data:{
      },
      success(data){
        //console.log(data.data.vote_demo_detail),
        that.setData({
          title:data.data.vote_demo.title,
          vote:data.data.vote_demo_detail,      
        })
      }
    }
    );

    /*wx.request({
      url: config.titleUrl,
      success: function (res) {
        console.log(res.data)
        that.setData({
          vote: res.data
        });
      }
    });*/
  },

  /**
   * 提交
   */
  formSubmit: function (e) {
    var that = this;
    var item = e.detail.value.item;
    if (!item) {
      console.log("未选中");
      wx.showToast({
        title: '未选中',
        icon: 'success'
      })
      return;
    }

    wx.request({
      //url: config.submitUrl,
      url: 'http://127.0.0.1:8000/submit',
      data: {
        ITEM: item,
        OPEN_ID: wx.getStorageSync('openid')
      },
      success: function (res) {
        if (res.data.RES) {
          wx.navigateTo({
            url: '/pages/result/result?VOTE_ID=' + 0,
          });
        } else {
          console.log("不能重复投票");
          wx.showToast({
            title: '不能重复投票',
            icon: 'success'
          })
        }

      }
    });
  },

  /**
   * 查看结果
   */
  showResult: function (e) {
    var that = this;
    wx.navigateTo({
      url: '/pages/result/result?VOTE_ID=' + 0,
    });
  }

});