import jQuery from 'jquery'

const DemoListItem = {
  el: '.js-DemoListItem',
  els: {
    link: '.js-DemoListItem-link'
  },

  init () {
    this.$el = jQuery(this.el)
    this.$el.find(this.els.link).on('click', jQuery.proxy(this.onLinkClick, this))
  },

  onLinkClick (e) {
    e.preventDefault()
    this.$el.find(this.els.link).removeClass('is-active')
    this.$el.find(e.target).addClass('is-active')
    alert(`"${e.target.textContent.trim()}" clicked`) // eslint-disable-line no-undef
  }
}

export default DemoListItem
