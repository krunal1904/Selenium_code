from xml.dom import minidom
from pathlib import Path

def resdXMLAsPerNode(your_test_param):
    first_parse_XML = minidom.parse(str(Path(__file__).parent.parent) + "/testData/testData.xml")
    data = first_parse_XML.getElementsByTagName(your_test_param)[0]
    return data.firstChild.data


def validatePrimaryMenusByXpath(linkName):
    return "(//a[contains(.,'" + linkName + "')])[1]"