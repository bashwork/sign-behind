/*
 * wrapper for the instragram api
 * http://instagram.com/developer/
 *
 * @author  bashwork at gmail dot com
 * @date    right about now
 * @license steal and be glad
 */
(function($) {

  var base = "https://api.instagram.com/v1/";
  var options = { access_token : 'token' };

  $.instagram = {};

    /**
     * @param opts The options to initialize with
     */
  $.instagram.initialize = function(opts) {
    $.extend(options, opts);
  };

  $.instagram.users = {
    /**
     * @param id The user unique identifier
     * @param callback Where the results should be sent
     */
    get : function(id, callback) {
      $.getJSON(base + 'users/' + id + '/?callback=?',
        options, callback);
    },

    /**
     * @param id The user unique identifier
     * @param query = {
     *   max_id
     *   min_id
     *   min_timestamp
     *   max_timestamp
     * }
     * @param callback Where the results should be sent
     */
    media : function(id, query, callback) {
      $.getJSON(base + 'users/' + id + '/media/recent/?callback=?',
        $.extend({}, options, query), callback);
    },

    /**
     * @param query = {
     *   q
     * }
     * @param callback Where the results should be sent
     */
    search : function(query, callback) {
      $.getJSON(base + 'users/search?callback=?',
        $.extend({}, options, query), callback);
    }
  };

  $.instragram.media = {
    /**
     * @param id The media unique identifier
     * @param callback Where the results should be sent
     */
    get : function(id, callback) {
      $.getJSON(base + 'media/' + id + '/?callback=?',
        options, callback);
    },

    /**
     * @param callback Where the results should be sent
     */
    popular : function(callback) {
      $.getJSON(base + 'media/popular?callback=?',
        options, callback);
    },

    /**
     * @param query = {
     *   lat            : Latitude of the center search coordinate
     *   lng            : Longitude of the center search coordinate
     *   max_timestamp  : A unix timestamp, media earlier than this timestamp
     *   min_timestamp  : A unix timestamp, media later than this timestamp
     *   distance       : Default is 1km (distance=1000), max distance is 5km
     * }
     * @param callback Where the results should be sent
     */
    search : function(query, callback) {
      $.getJSON(base + 'users/search?callback=?',
        $.extend({}, options, query), callback);
    }
  };

  $.instragram.likes = {
    /**
     * @param id The media unique identifier
     * @param callback Where the results should be sent
     */
    get : function(id, callback) {
      $.getJSON(base + 'media/' + id + '/likes?callback=?',
        options, callback);
    }
  };

  $.instragram.comments = {
    /**
     * @param id The media unique identifier
     * @param callback Where the results should be sent
     */
    get : function(id, callback) {
      $.getJSON(base + 'media/' + id + '/comments?callback=?',
        options, callback);
    }
  };

  $.instragram.tags = {
    /**
     * @param name The tag to retrieve information for
     * @param callback Where the results should be sent
     */
    get : function(name, callback) {
      $.getJSON(base + 'tags/' + name + '?callback=?',
        options, callback);
    },

    /**
     * @param name The tag to retrieve information for
     * @param callback Where the results should be sent
     */
    recent : function(name, callback) {
      $.getJSON(base + 'tags/' + name + '/media/recent?callback=?',
        options, callback);
    },

    /**
     * @param name The tag to retrieve information for
     * @param callback Where the results should be sent
     */
    search : function(query, callback) {
      $.getJSON(base + 'tags/search?callback=?',
        $.extend({}, options, {q : query}), callback);
    }
  };

  $.instragram.locations = {
    /**
     * @param id The unique location identifier
     * @param callback Where the results should be sent
     */
    get : function(id, callback) {
      $.getJSON(base + 'locations/' + id + '?callback=?',
        options, callback);
    },

    /**
     * @param id The unique location identifier
     * @param query = {
     *   max_id
     *   min_id
     *   min_timestamp
     *   max_timestamp
     * }
     * @param callback Where the results should be sent
     */
    recent : function(id, query, callback) {
      $.getJSON(base + 'locations/' + id + '/media/recent?callback=?',
        $.extend({}, options, query), callback);
    },

    /**
     * @param query = {
     *   lat            : Latitude of the center search coordinate
     *   lng            : Longitude of the center search coordinate
     *   foursquare_id  : A place's foursquare identifier
     *   distance       : Default is 1km (distance=1000), max distance is 5km
     * }
     * @param callback Where the results should be sent
     */
    search : function(query, callback) {
      $.getJSON(base + 'locations/search?callback=?',
        $.extend({}, options, query), callback);
    }
  };

})(jQuery);
