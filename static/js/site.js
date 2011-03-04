var site = {

  /**
   * @brief Method used to perform the instagram login
   * @param id The user client id to login with
   */
  login : function(id) {
    IG.init({
      client_id: id,
      check_status: false,
      logging: true
    });

    IG.login(function(response) {
      if (response.code) {
        document.location = '/instagram/callback?code=' + response.code;
      } else if (response.session) {
        document.location = '/instagram/load_user?ig_user_id=' + response.session.id;
      }
    }, {
      response_type: 'code',
      scope: ['comments', 'likes', 'relationships']
    });
  },

};
