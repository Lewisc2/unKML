#!/usr/bin/env python
import ACELayer
import logging

logging.basicConfig(format = '%(levelname)s: %(message)s', level = logging.INFO)
ACELayer.outputDir = 'output'

layers = [
  ACELayer.Layer('COP', 'http://weather.msfc.nasa.gov/ACE/latestALCOMCOP.kml')
]

ACELayer.Layer.processLayerList(layers)
