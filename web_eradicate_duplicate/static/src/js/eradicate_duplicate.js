/* Web Eradicate Duplicate
   @author: Alexis de Lattre <alexis.delattre@akretion.com>
   Inspired by the module web_hide_duplicate of Aristobulo Meneses
*/

odoo.define('web.web_eradicate_duplicate', function(require) {
    "use strict";

    var core = require('web.core');
    var FormView = require('web.FormView');
    var _t = core._t;

    FormView.include({
        render_sidebar: function($node) {
            this._super($node);
            // Remove Action > Duplicate button for all users except admin
            // or except if there is an attribute duplicate_eradicate="false"
            // in the form view
            if (
                    this.sidebar &&
                    this.sidebar.items &&
                    this.sidebar.items.other &&
                    this.session.uid != 1 &&
                    this.is_action_enabled('eradicate_duplicate')) {
                var new_items_other = _.reject(this.sidebar.items.other, function (item) {
                    return item.label === _t('Duplicate');
                });
                this.sidebar.items.other = new_items_other;
            }
        }
    });
});

/*

EXAMPLE : enable duplicate on account.move :

<record id="view_move_form" model="ir.ui.view">
    <field name="name">duplicate_allowed.account_move_form</field>
    <field name="model">account.move</field>
    <field name="inherit_id" ref="account.view_move_form"/>
    <field name="arch" type="xml">
        <xpath expr="/form" position="attributes">
            <attribute name="eradicate_duplicate">false</attribute>
        </xpath>
    </field>
</record>

*/
