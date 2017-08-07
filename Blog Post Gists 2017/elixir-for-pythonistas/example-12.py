def view_function(request, user, reports=None):
  reports = reports or {}
  for key, f in reports.items():
      perm_key = 'user.can_view_%s_report' % key
      if key == 'unsigned' and not user.sig_on:
          continue
      if key in ('foo', 'br') and not user.new_user:
          continue
      if key in ('payments', 'all', 'client') and not user.track:
          continue
      if key == 'authorizations' and not user.cms_user:
          continue
      if key == 'totalcostof' and not user.is_foobar:
          continue
      if key == 'premiums' and not \
              (user.some_attribute and request.user.admin and request.user.admin.is_manager):
          continue
