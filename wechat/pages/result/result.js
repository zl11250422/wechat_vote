var config = require( '../../utils/config.js' );

Page( {
    data: {
    },
    onLoad: function( options ) {
        var voteId = options.VOTE_ID;
        var that = this;
        //获取投票结果
        wx.request( {
            url: 'http://127.0.0.1:8000/result',
            data: {
                VOTE_ID: voteId,
                OPEN_ID: wx.getStorageSync( 'openid' )
            },
            success: function( res ) {
                console.log( res.data.vote_demo_detail )
                console.log(res.data.total_size)
                console.log(res.data.current_vote)
                that.setData( {
                    vote: res.data.vote_demo_detail,
                    total_size: res.data.total_size,
                    current_vote: res.data.current_vote
                });
            }
        });
    },
    back: function( e ) {
        wx.navigateBack();
    }
})