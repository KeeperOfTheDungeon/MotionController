package de.hska.lat.ant.metaData;

import de.hska.lat.perception.fieldOfView.FieldOfViewMetaData;


public enum AntFieldOfViews 
{
	LUX("lux"),
	;
	
	
	/**
	 * @uml.property  name="name"
	 */
	String name;

	
	AntFieldOfViews(String name)
{
	this.name=name;
}
	


public FieldOfViewMetaData getMetaData()
{
	return(new FieldOfViewMetaData(this.name,this.name(), (byte)this.ordinal()));
}


public byte getId()
{
	return ((byte) this.ordinal());
}


}
