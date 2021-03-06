# Copyright (C) 2004-2016 Kevin E. Gilbert, dba Serena Software
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Kevin E. Gilbert
# Serena Software
# Box 3076
# Bloomington, IN 47402-3076
#
# gilbert@serenasoft.com

#ifndef NONBOND_H
#define NONBOND_H

struct t_nonbond {
        int nonbond, npair, maxnbtype, **iNBtype, **ipif;
        float **vrad, **veps, **vrad14,**veps14;
        } nonbond;
          
 /* EXTERN struct t_nonbond {
        int nonbond, npair, ntype, *iNBtype;
        float *vrad, *veps, *ipif;
        } nonbond;  */


/* EXTERN struct t_nonbond {
        int nonbond, iNB[MAXNB][3];
        float vrad[MAXNB], veps[MAXNB];
        } nonbond;  */
#endif
