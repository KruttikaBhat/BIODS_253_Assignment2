#!/usr/bin/env python3
"""
test_drawing.py

Unit tests for the drawing functions in drawing.py. Each test sets up an
SVG canvas using svg_turtle, calls the corresponding drawing function, and
then compares the generated image to the expected image saved in testdata/.
"""

import os
import tempfile
import unittest
import inspect

import svg_turtle
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import matplotlib.testing.compare as mpcompare

import drawing  # your drawing module (with draw_cloud, draw_rectangle, etc.)

CANVAS_SIZE = (500, 500)
TOLERANCE = 1.0  # allowed difference between images (0.0 means exact)

class TestDrawingFunctions(unittest.TestCase):

    def _compare_canvas_to_expected(self, expected_filename, override_tmpdir=None):
        """
        Save the current canvas as an SVG and convert to PNG.
        Compare the resulting image with the expected image.
        Returns None if and only if the images are identical.
        """
        with tempfile.TemporaryDirectory() as tmp_dirname:
            # Use the name of the calling function as part of the temporary filename.
            calling_function = inspect.stack()[1][3]
            tmp_dirname = tmp_dirname if not override_tmpdir else override_tmpdir
            actual_svg = os.path.join(tmp_dirname, f'{calling_function}.svg')
            actual_png = os.path.join(tmp_dirname, f'{calling_function}.png')
            self._turtle.save_as(actual_svg)
            drawing_obj = svg2rlg(actual_svg)
            renderPM.drawToFile(drawing_obj, actual_png, fmt="PNG")
            return mpcompare.compare_images(expected_filename, actual_png, TOLERANCE)

    def setUp(self):
        # Create an SVG-based turtle canvas.
        self._turtle = svg_turtle.SvgTurtle(*CANVAS_SIZE)
        # Monkey-patch the drawing module's turtle so that drawing functions use our canvas.
        drawing.turtle = self._turtle
        # Clear the canvas before each test.
        self._turtle.reset()

    def test_draw_cloud(self):
        drawing.draw_cloud(50, 50, size=40)
        result = self._compare_canvas_to_expected('testdata/draw_cloud.png')
        self.assertIsNone(result, msg="draw_cloud output does not match expected image.")

    def test_draw_rectangle(self):
        drawing.draw_rectangle(-50, -50, 100, 100, color="blue")
        result = self._compare_canvas_to_expected('testdata/draw_rectangle.png')
        self.assertIsNone(result, msg="draw_rectangle output does not match expected image.")

    def test_draw_triangle(self):
        drawing.draw_triangle(0, 0, 100, "yellow")
        result = self._compare_canvas_to_expected('testdata/draw_triangle.png')
        self.assertIsNone(result, msg="draw_triangle output does not match expected image.")

    def test_draw_tree(self):
        # Adjusted call: the tree is now drawn at (0, -50) so it isn't cut off.
        drawing.draw_tree(0, -50, trunk_width=20, trunk_height=40, foliage_base=60)
        result = self._compare_canvas_to_expected('testdata/draw_tree.png')
        self.assertIsNone(result, msg="draw_tree output does not match expected image.")

if __name__ == '__main__':
    unittest.main()