%define _use_internal_dependency_generator 0

Summary:	Chapeau meta-package for bumblebee nvidia prorietory drivers
Name:		chapeau-bumblebee-nonfree
Version:	1
Release:	2%{?dist}
License:	GPL v2
Group:		Chapeau
URL:		http://chapeaulinux.org
BuildArch:	x86_64

Requires:	bumblebee-nonfree-release
Requires:	libbsd-devel
Requires:	libbsd
Requires:	glibc-devel
Requires:	libX11-devel
Requires:	help2man
Requires:	autoconf
Requires:	git
Requires:	tar
Requires:	glib2
Requires:	glib2-devel
Requires:	kernel-devel
Requires:	kernel-headers
Requires:	automake
Requires:	gcc
Requires:	gtk2-devel
Requires:	bbswitch-dkms
Requires:	bumblebee-nvidia
Requires:	VirtualGL
Requires:	VirtualGL(x86-32)
Requires:	primus
Requires:	primus(x86-32)

%description
A meta package which requires the bumblebee nonfree nvidia drivers packages

%prep

%build

%clean 

%install

%post

%preun
[ $0 = 1 ]] && rpm -e bumblebee-nvidia VirtualGL.x86_64 VirtualGL.i686 primus.x86_64 primus.i686 bbswitch-dkms

%files 


%changelog
* Sun Nov 22 2015 Vince Pooley <vince@chapeaulinux.org>
- Incorrect architecture declarations fixed

* Fri Nov 20 2015 Vince Pooley <vince@chapeaulinux.org>
- initial release

