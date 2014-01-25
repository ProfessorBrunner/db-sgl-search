Select ER.objid, ER.ra, ER.dec from MyDB.ER_file as ER
  Join Neighbors as N on ER.objid = N.objid
  Where N.distance between ER.maxER+.025 and ER.minER-.025 /*Some of the estimates are the same*/ 

