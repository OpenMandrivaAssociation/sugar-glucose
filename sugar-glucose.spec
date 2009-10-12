# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name: sugar-glucose
Version: 0.86.2
Release: %mkrel 1
Summary: Core Sugar components
License: GPL/LGPL
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Requires: sugar-artwork >= 0.86.0
Requires: sugar-datastore >= 0.86.1
Requires: sugar-presence-service >= 0.86.0
Requires: sugar >= 0.86.2
Requires: sugar-base >= 0.86.0
Requires: sugar-toolkit >= 0.86.1

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Virtual package of core Sugar components that follow the Sugarlabs
six months release schedule.
Sugar is a graphical user interface aimed at children which promotes sharing
and collaborative learning. It was introduced on the One Laptop Per Child
(OLPC) XO laptop but is useful on other devices as well.

%files
%defattr(-,root,root,-)

