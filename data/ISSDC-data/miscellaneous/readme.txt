miscellaneous collection contents
=======================================================================================       
                                                                              
The directory Structure and contents for miscellaneous directory is                  
same as that of data directory.                  
                                                                              
The miscellaneous directory contains follwings files which are describe              
as follows                                                                    
                                                                              
-------------------------------------------------------------------------------------                                                                             
1. Orbit and Attitude Header File                                             
-------------------------------------------------------------------------------------      
Orbit and Attitude Header File from URSC Level-0 Directory File   
ch2_<inst>_<mtc>_<YYYYMMDDTHHMMSSssss>_<p>_<prd>_<stn>.oath                  
The OATH File has 201 bytes ASCII Text File
file format is as follows

Sr. No. 	     Description	                        Format	       Bytes
=======================================================================================
1	    Record type ("ORBTATTD-HDR")	                 A12	         12
2	    Project name ("CHANDRAYAAN-2 MISSION")	         A21	         21
3	    Block length in bytes for Header 	                 I6	          6
4	    Station Identification ("BLR$/JPL$...")	         A4	          4
5	    Start UTC time for First OAT  block(Note-5)	         7I4	         28
6	    End  UTC time for Last OAT  block(Note-5)	         7I4	         28
7	    Number of OAT records	                         I6	          6
8	    Record length of OAT data (not including header)	 I6	          6
9	    Source for attitude values - Note-1	                 I1	          1
10	    Mission Phase (Earth/Lunar - Centered) - Note-2	 I1	          1
11	    Spare		                                                 88
=======================================================================================
                                               Total	                        201

Note-1: 
1 - Attitude from SS1
2 - Attitude from SS2
3 - Attitude from ECI QS

Note-2:
1-Earth Centered (Earth Bound Phase)
3-Moon Centered (Lunar Phase)

Note-5:

UTC in OAT file is mentioned with Millisecond 	resolution as 	following:

YYYYDDDDMMMMHHHHMMMMSSSSMMMM

Space filling is used if value is less than 4 digits. 

Exp: 2013  10  22   1  22   4 402

Year-2013
Month-10
Date-22
Hour-1
Minute-22
Sec-4
Millisec-402  
 
-------------------------------------------------------------------------------------                                                                             
2. Orbit and Attitude Data File Format
-------------------------------------------------------------------------------------
Orbit and Attitude File is provided by URSC Level-0 Team.
ch2_<inst>_<mtc>_<YYYYMMDDTHHMMSSssss>_<p>_<prd>_<stn>.oat 
This file is generated in ASCII format. OAT is provided 
at every 512 millisecond interval for payload duration.
The OAT File has 628 bytes ASCII Text File.
file format is as follows

Sr. No.	       Description	                                              Format  Bytes
================================================================================================
1	Record type ("ORBTATTD")	                                       A8	8
2	Physical record number in this file	                               I6	6
3	Block length in bytes	                                               I4	4
4	Time in UTC	                                                       7I4	28
5	Lunar Position X (kms) - J2000 Earth Centre Frame 	               F20.6	20
6	Lunar Position Y (kms) - J2000 Earth Centre Frame	               F20.6	20
7	Lunar Position Z (kms) - J2000 Earth Centre Frame	               F20.6	20
8	Satellite position X (kms) - Note-3	                               F20.6	20
9	Satellite position Y (kms) - Note-3	                               F20.6	20
10	Satellite position Z (kms) - Note-3	                               F20.6	20
11	Satellite velocity X-dot (kms/sec) - Note-3	                       F12.6	12
12	Satellite velocity Y-dot (kms/sec) - Note-3	                       F12.6	12
13	Satellite velocity Z-dot (kms/sec)  - Note-3	                       F12.6	12
14	S/C Attitude - Inertial to Body Q1, Q2, Q3 and Q4	               4F14.10	56
15	Transformation Quaternion for Earth Fixed IAU frame Q1,Q2,Q3,Q4	       4F14.10	56
16	Transformation Quaternion for Lunar Fixed IAU frame Q1,Q2,Q3,Q4	       4F14.10	56
17	Latitude of sub-satellite point (deg) 	                               F14.8	14
18	Longitude of sub-satellite point (deg	                               F14.8	14
19	Solar Azimuth                	                                       F14.8	14
20	Solar Elevation          	                                       F14.8	14
21	Latitude  (deg)	                               			       F14.8	14
22	Longitude (deg)	                                                       F14.8	14
23	Satellite altitude (kms) 	                                       F12.3	12
24	Angle between +Roll and Velocity Vector	                               F12.3	12
25	Eclipse Status - Note-4	                                               I1	1
26	Emission Angle	                                                       F9.3	9
27	Sun Angle w.r.t -ve Yaw (Phase angle) 	                               F9.3	9
28	Angle between +Yaw and Nadir	                                       F9.3	9
29	Slant Range (Km) 	                                               F10.3	10
30	Orbit No 	                                                       I5	5
31	Solar Zenith Angle	                                               F9.3	9
32	Angle between Payload FoV axis and velocity vector	               F9.3	9
33	X  (yaw) angle	                                                       F16.8	16
34	Y  (roll) angle	                                                       F16.8	16
35	Z(pitch) angle 	                                                       F16.8	16
36	Spare		                                                                41
===============================================================================================
                                                    Total	                       628

Note-3: EME J2000 frame of reference, refer Sl. No. 10 of Header for center (Earth/Moon) 

Note-4: Eclipse Status 
		0 - No Eclipse
		1 - Umbra
		2 - Penumbra

------------------------------------------------------------------------------------------------
3. Liberation angle Data File Format                                               
------------------------------------------------------------------------------------------------      
Liberation angle Data File with lbr extension from URSC Level-0 team. 
ch2_<inst>_<mtc>_<YYYYMMDDTHHMMSSssss>_<p>_<prd>_<stn>.lbr
The LBR File has 258 bytes ASCII Text File. 
file format is as follows

Sr. No.	Description	                                                      Format	Bytes
================================================================================================
1	Record type ("ORBTATTD")	                                        A8	8
2	Physical record number in this file	                                I6	6
3	Block length in bytes	                                                I4	4
4	Time in UTC	                                                        7I4	28
5	Satellite position X (kms) - Note-3	                                F20.6	20
6	Satellite position Y (kms) - Note-3	                                F20.6	20
7	Satellite position Z (kms) - Note-3	                                F20.6	20
8	Satellite velocity X-dot (kms/sec) - Note-3	                        F12.6	12
9	Satellite velocity Y-dot (kms/sec) - Note-3	                        F12.6	12
10	Satellite velocity Z-dot (kms/sec)  - Note-3	                        F12.6	12
11	Liberation angle - Phi 	                                                F16.8	16
12	Liberation angle - Psi	                                                F16.8	16
13	Liberation angle - Theta	                                        F16.8	16
14	Liberation angle - Phi Rate	                                        F12.6	12
15	Liberation angle - Psi Rate	                                        F12.6	12
16	Liberation angle - Theta Rate	                                        F12.6	12
17	Spare		                                                                32
===============================================================================================
                                                          Total	                       258

Note-3: J2000 frame of reference with moon as center 
                                  

4. Sun Angle File Format                                                    
------------------------------------------------------------------------      
Liberation angle Data File with lbr extension from URSC Level-0 team. 
ch2_<inst>_<mtc>_<YYYYMMDDTHHMMSSssss>_<p>_<prd>_<stn>.spm
The LBR File has 249 bytes ASCII Text File.
file format is as follows

Sr. No.	Description	                                                   Format     Bytes
================================================================================================
1	Record type ("ORBTATTD")	                                     A8	        8
2	Physical record number in this file	                             I6	        6
3	Block length in bytes	                                             I4	        4
4	Time in UTC	                                                     7I4	28
5	Satellite position X (kms) - Note-3	                             F20.6	20
6	Satellite position Y (kms) - Note-3	                             F20.6	20
7	Satellite position Z (kms) - Note-3	                             F20.6	20
8	Satellite velocity X-dot (kms/sec) - Note-3	                     F12.6	12
9	Satellite velocity Y-dot (kms/sec) - Note-3	                     F12.6	12
10	Satellite velocity Z-dot (kms/sec)  - Note-3	                     F12.6	12
11	Phase angle 	                                                     F9.3	9
12	Sun aspect	                                                     F9.3	9
13	Sun Azimuth	                                                     F9.3	9
14	Sun Elevation	                                                     F9.3	9
15	Orbit Limb Direction - Note 5	                                     I1	        1
17	Spare		                                                                70
=================================================================================================
                                                              Total	                249

Solar Incidence Angles can be computed by following steps:

i. Read and extracting the Sun Elevation from sun parameter file 
ii. Solar Incidence Angle = 90 - Sun Elevation Angle
