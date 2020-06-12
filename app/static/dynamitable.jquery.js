!function($){ 'use strict';

    $.fn.dynamitable = function(options) {
    
        /**********************************************
         * dynamitable
         **********************************************/
        var dynamitable = this;
        
        /**********************************************
         * dynamitableCore
         **********************************************/
        var dynamitableCore = new (function($dynamitable) {
        
            /**********************************************
             * dynamitableCore.getIndex($field)
             *
             * get the index of a field
             *
             * return integer
             **********************************************/
            this.getIndex = function($field) {
                return $field.parents('tr').children('td, th').index($field);
            };
            
            /**********************************************
             * dynamitableCore.getBody()
             *
             * get the body of the table
             *
             * return dom
             **********************************************/
            this.getBody = function() {
                return $dynamitable.find('tbody');
            };
            
            /**********************************************
             * dynamitableCore.getRows()
             *
             * get all row inside the body of the table
             *
             * return dom
             **********************************************/
            this.getRows = function() {
                return this.getBody().children('tr');
            };
            
            /**********************************************
             * dynamitableCore.getField(index, $row)
             *
             * get a field
             *
             * return dom
             **********************************************/
            this.getField = function(index, $row) {
                return $row.children('td, th').eq(index);
            };
            
            /**********************************************
             * dynamitableCore.getValue(index, $row)
             *
             * get a field value
             *
             * return string
             **********************************************/
            this.getValue = function(index, $row) {
                return this.getField(index, $row).text();
            };
            
        })($(this));   
        
        /**********************************************
         * dynamitable.filterList
         *
         * list of filter selector
         *
         * array of string
         **********************************************/
        this.filterList = [];
        
        /**********************************************
         * dynamitable.displayAll()
         *
         * show all <tr>
         *
         * return dynamitable
         **********************************************/
        this.displayAll = function() {

            dynamitableCore.getRows().each(function() {
                $(this).show();
            });
          
            return this;
        };

        /**********************************************
         * dynamitable.filter(index, matches)
         *
         * hide all <tr> that doen't martch
         *
         * - index (integer): index of the colum to filter
         * - matches (string)  : string to search on the colum
         *
         * return dynamitable
         **********************************************/
        this.filter = function filter(index, matches) {
        
            var regex = new RegExp(matches, 'i');
            
            dynamitableCore.getRows().each(function () {
                if(true !== regex.test(dynamitableCore.getValue(index, $(this)))) {
                    $(this).hide();
                }
            });
          
            return this;
        };
        
        /**********************************************
         * dynamitable.addFilter(selector)
         *
         * add filter event on element inside the table heading
         *
         * - selector (string) : selector of the element that trigger the event
         *
         * return dynamitable
         **********************************************/
        this.addFilter = function addFilter(selector) {
        
            // add the selector on the filter list
            dynamitable.filterList.push(selector);
            
            // the filter
            var filterAction = function() {
            
                 dynamitable.displayAll();
                 
                 $(dynamitable.filterList).each(function(index, selector) {
                 
                    $(dynamitable).find(selector).each(function() {
                        var $this =  $(this);
                        dynamitable.filter(dynamitableCore.getIndex($this.parent('td, th')), $this.val());  
                    });
                 
                 });
            };
            
            // attach the filter action to the selector
            $(selector).on('change keyup keydown', filterAction);
            
            // initialization
            filterAction();
            
            return this;
        }; 
        
        /**********************************************
         * dynamitable.addSorter(selector, order)
         *
         * add soter event on element inside the table heading
         *
         * - selector (string) : selector of the element that trigger the event
         * - order (string) :  sorting order [asc, desc]
         *
         * return dynamitable
         **********************************************/
        this.addSorter = function addSorter(selector, order) {

            $(dynamitable).find(selector).each(function() {
                var $this = $(this);
                
                var index = dynamitableCore.getIndex($this.parent('td, th'));
                
                $this.on('click', function() { dynamitable.sorter(index, order); });
            });
            
            return this;
        }; 
    
        /**********************************************
         * dynamitable.sorter(index, order)
         *
         * - index (integer): index of the colum to sorter
         * - order (string)  : sorting order [asc, desc]
         *
         * return dynamitable
         **********************************************/
        this.sorter = function sorter(index, order) {

           dynamitableCore.getBody().append(dynamitableCore.getRows().detach().sort(function(row_a, row_b) {

                var value_a = dynamitableCore.getValue(index, $(row_a));
                var value_b = dynamitableCore.getValue(index, $(row_b));
                
                var order_desc = ('desc' === order) ? true : false;
                
                // numeric order mode
                if(value_a.replace(/[^\d-]/g, '') !== '' && value_b.replace(/[^\d-]/g, '') !== '') {
                    value_a = parseFloat(value_a.replace(/[^\d,.-+]/g, ''));
                    value_b = parseFloat(value_b.replace(/[^\d,.-+]/g, ''));
                }
                
                if(value_a === value_b) {
                    return 0;
                }

                return (value_a > value_b) ? order_desc ? 1 : -1 : order_desc ? -1 : 1;

            }));
            
            return this;
        };
          
        return this;
    };
    
    /**********************************************
     * Dynamitable trigger
     **********************************************/
    $(document).find('.js-dynamitable').each(function(){
    
        $(this).dynamitable()
            .addFilter('.js-filter')
            .addSorter('.js-sorter-asc', 'asc')
            .addSorter('.js-sorter-desc', 'desc')
        ;
    });

}(jQuery);