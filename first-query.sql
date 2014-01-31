SELECT pt.objid, pt.ra, pt.dec, pz.z, SM.minLogMass, SM.maxLogMass,t.NeighborObjID t.distance from (

SELECT obj.objid, COUNT(*) as numNeighbors
FROM
( 
SELECT g.objid, N.NeighborObjID
FROM Galaxy AS G
JOIN Neighbors AS N ON G.ObjID = N.ObjID 
WHERE 
((cModelMag_i-extinction_i between 17.5 and 19.9
and dered_r-dered_i-(dered_g-dered_r)/8. > 0.55
and dered_r-dered_i < 2
and cModelMag_i-extinction_i < 19.86+1.6*( dered_r-dered_i-(dered_g-dered_r)/8.-0.8)
and fiber2Mag_i-extinction_i < 21.5
and psfMag_i-ModelMag_i > 0.2+0.2*(20.0-dered_i)
and psfMag_z-ModelMag_z > 9.125-0.46*dered_z 
) 
OR
(dered_r-dered_i-(dered_g-dered_r)/4. -.18 between -.2 and .2
  and cModelMag_r-extinction_r < 13.8+( 0.7*(dered_g-dered_r)+1.2*(dered_r-dered_i-.18))/.3
  and cModelMag_r-extinction_r between 16 and 19.6
  and psfMag_r-cModelMag_r > 0.3)
) 
 And N.distance<.3
 )
AS obj

JOIN PhotoPrimary AS p ON p.ObjID = obj.NeighborObjID
WHERE 
p.u - p.g < 1 AND
p.g - p.r < 1
GROUP BY obj.objid
HAVING COUNT(obj.objid) > 0
) as t
  JOIN PhotoPrimary as pt on pt.objid = t.objid
  JOIN PhotoZ as pz on pz.objID = t.objID
JOIN stellarMassPassivePort as SM on SM.specObjID = pt.specObjID

