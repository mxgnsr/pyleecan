# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/MeshVTK.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/MeshVTK
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Mesh import Mesh

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.MeshVTK.get_mesh_pv import get_mesh_pv
except ImportError as error:
    get_mesh_pv = error

try:
    from ..Methods.Mesh.MeshVTK.get_point import get_point
except ImportError as error:
    get_point = error

try:
    from ..Methods.Mesh.MeshVTK.get_cell import get_cell
except ImportError as error:
    get_cell = error

try:
    from ..Methods.Mesh.MeshVTK.get_normals import get_normals
except ImportError as error:
    get_normals = error

try:
    from ..Methods.Mesh.MeshVTK.get_surf import get_surf
except ImportError as error:
    get_surf = error

try:
    from ..Methods.Mesh.MeshVTK.get_cell_area import get_cell_area
except ImportError as error:
    get_cell_area = error

try:
    from ..Methods.Mesh.MeshVTK.convert import convert
except ImportError as error:
    convert = error


from cloudpickle import dumps, loads
from ._check import CheckTypeError

try:
    from pyvista.core.pointset import UnstructuredGrid
except ImportError:
    UnstructuredGrid = ImportError
try:
    from pyvista.core.pointset import PolyData
except ImportError:
    PolyData = ImportError
from ._check import InitUnKnowClassError


class MeshVTK(Mesh):
    """Gather the mesh storage format"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.MeshVTK.get_mesh_pv
    if isinstance(get_mesh_pv, ImportError):
        get_mesh_pv = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method get_mesh_pv: " + str(get_mesh_pv))
            )
        )
    else:
        get_mesh_pv = get_mesh_pv
    # cf Methods.Mesh.MeshVTK.get_point
    if isinstance(get_point, ImportError):
        get_point = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method get_point: " + str(get_point))
            )
        )
    else:
        get_point = get_point
    # cf Methods.Mesh.MeshVTK.get_cell
    if isinstance(get_cell, ImportError):
        get_cell = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method get_cell: " + str(get_cell))
            )
        )
    else:
        get_cell = get_cell
    # cf Methods.Mesh.MeshVTK.get_normals
    if isinstance(get_normals, ImportError):
        get_normals = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method get_normals: " + str(get_normals))
            )
        )
    else:
        get_normals = get_normals
    # cf Methods.Mesh.MeshVTK.get_surf
    if isinstance(get_surf, ImportError):
        get_surf = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method get_surf: " + str(get_surf))
            )
        )
    else:
        get_surf = get_surf
    # cf Methods.Mesh.MeshVTK.get_cell_area
    if isinstance(get_cell_area, ImportError):
        get_cell_area = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshVTK method get_cell_area: " + str(get_cell_area)
                )
            )
        )
    else:
        get_cell_area = get_cell_area
    # cf Methods.Mesh.MeshVTK.convert
    if isinstance(convert, ImportError):
        convert = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method convert: " + str(convert))
            )
        )
    else:
        convert = convert
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        mesh=None,
        is_pyvista_mesh=False,
        format="vtk",
        path="",
        name="mesh",
        surf=None,
        is_vtk_surf=False,
        surf_path="",
        surf_name="surf",
        label=None,
        dimension=2,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            mesh = obj.mesh
            is_pyvista_mesh = obj.is_pyvista_mesh
            format = obj.format
            path = obj.path
            name = obj.name
            surf = obj.surf
            is_vtk_surf = obj.is_vtk_surf
            surf_path = obj.surf_path
            surf_name = obj.surf_name
            label = obj.label
            dimension = obj.dimension
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "mesh" in list(init_dict.keys()):
                mesh = init_dict["mesh"]
            if "is_pyvista_mesh" in list(init_dict.keys()):
                is_pyvista_mesh = init_dict["is_pyvista_mesh"]
            if "format" in list(init_dict.keys()):
                format = init_dict["format"]
            if "path" in list(init_dict.keys()):
                path = init_dict["path"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "surf" in list(init_dict.keys()):
                surf = init_dict["surf"]
            if "is_vtk_surf" in list(init_dict.keys()):
                is_vtk_surf = init_dict["is_vtk_surf"]
            if "surf_path" in list(init_dict.keys()):
                surf_path = init_dict["surf_path"]
            if "surf_name" in list(init_dict.keys()):
                surf_name = init_dict["surf_name"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
        # Initialisation by argument
        # Check if the type UnstructuredGrid has been imported with success
        if isinstance(UnstructuredGrid, ImportError):
            raise ImportError("Unknown type UnstructuredGrid please install pyvista")
        self.mesh = mesh
        self.is_pyvista_mesh = is_pyvista_mesh
        self.format = format
        self.path = path
        self.name = name
        # Check if the type PolyData has been imported with success
        if isinstance(PolyData, ImportError):
            raise ImportError("Unknown type PolyData please install pyvista")
        self.surf = surf
        self.is_vtk_surf = is_vtk_surf
        self.surf_path = surf_path
        self.surf_name = surf_name
        # Call Mesh init
        super(MeshVTK, self).__init__(label=label, dimension=dimension)
        # The class is frozen (in Mesh init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MeshVTK_str = ""
        # Get the properties inherited from Mesh
        MeshVTK_str += super(MeshVTK, self).__str__()
        MeshVTK_str += "mesh = " + str(self.mesh) + linesep + linesep
        MeshVTK_str += "is_pyvista_mesh = " + str(self.is_pyvista_mesh) + linesep
        MeshVTK_str += 'format = "' + str(self.format) + '"' + linesep
        MeshVTK_str += 'path = "' + str(self.path) + '"' + linesep
        MeshVTK_str += 'name = "' + str(self.name) + '"' + linesep
        MeshVTK_str += "surf = " + str(self.surf) + linesep + linesep
        MeshVTK_str += "is_vtk_surf = " + str(self.is_vtk_surf) + linesep
        MeshVTK_str += 'surf_path = "' + str(self.surf_path) + '"' + linesep
        MeshVTK_str += 'surf_name = "' + str(self.surf_name) + '"' + linesep
        return MeshVTK_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Mesh
        if not super(MeshVTK, self).__eq__(other):
            return False
        if other.mesh != self.mesh:
            return False
        if other.is_pyvista_mesh != self.is_pyvista_mesh:
            return False
        if other.format != self.format:
            return False
        if other.path != self.path:
            return False
        if other.name != self.name:
            return False
        if other.surf != self.surf:
            return False
        if other.is_vtk_surf != self.is_vtk_surf:
            return False
        if other.surf_path != self.surf_path:
            return False
        if other.surf_name != self.surf_name:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Mesh
        MeshVTK_dict = super(MeshVTK, self).as_dict()
        if self.mesh is None:
            MeshVTK_dict["mesh"] = None
        else:  # Store serialized data (using cloudpickle) and str to read it in json save files
            MeshVTK_dict["mesh"] = {
                "__class__": str(type(self._mesh)),
                "__repr__": str(self._mesh.__repr__()),
                "serialized": dumps(self._mesh).decode("ISO-8859-2"),
            }
        MeshVTK_dict["is_pyvista_mesh"] = self.is_pyvista_mesh
        MeshVTK_dict["format"] = self.format
        MeshVTK_dict["path"] = self.path
        MeshVTK_dict["name"] = self.name
        if self.surf is None:
            MeshVTK_dict["surf"] = None
        else:  # Store serialized data (using cloudpickle) and str to read it in json save files
            MeshVTK_dict["surf"] = {
                "__class__": str(type(self._surf)),
                "__repr__": str(self._surf.__repr__()),
                "serialized": dumps(self._surf).decode("ISO-8859-2"),
            }
        MeshVTK_dict["is_vtk_surf"] = self.is_vtk_surf
        MeshVTK_dict["surf_path"] = self.surf_path
        MeshVTK_dict["surf_name"] = self.surf_name
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MeshVTK_dict["__class__"] = "MeshVTK"
        return MeshVTK_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.mesh = None
        self.is_pyvista_mesh = None
        self.format = None
        self.path = None
        self.name = None
        self.surf = None
        self.is_vtk_surf = None
        self.surf_path = None
        self.surf_name = None
        # Set to None the properties inherited from Mesh
        super(MeshVTK, self)._set_None()

    def _get_mesh(self):
        """getter of mesh"""
        return self._mesh

    def _set_mesh(self, value):
        """setter of mesh"""
        try:  # Check the type
            check_var("mesh", value, "dict")
        except CheckTypeError:
            check_var("mesh", value, "pyvista.core.pointset.UnstructuredGrid")
            # property can be set from a list to handle loads
        if (
            type(value) == dict
        ):  # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._mesh = loads(value["serialized"].encode("ISO-8859-2"))
        else:
            self._mesh = value

    mesh = property(
        fget=_get_mesh,
        fset=_set_mesh,
        doc=u"""Pyvista object of the mesh (optional)

        :Type: pyvista.core.pointset.UnstructuredGrid
        """,
    )

    def _get_is_pyvista_mesh(self):
        """getter of is_pyvista_mesh"""
        return self._is_pyvista_mesh

    def _set_is_pyvista_mesh(self, value):
        """setter of is_pyvista_mesh"""
        check_var("is_pyvista_mesh", value, "bool")
        self._is_pyvista_mesh = value

    is_pyvista_mesh = property(
        fget=_get_is_pyvista_mesh,
        fset=_set_is_pyvista_mesh,
        doc=u"""Store the pyvista object

        :Type: bool
        """,
    )

    def _get_format(self):
        """getter of format"""
        return self._format

    def _set_format(self, value):
        """setter of format"""
        check_var("format", value, "str")
        self._format = value

    format = property(
        fget=_get_format,
        fset=_set_format,
        doc=u"""Format in which the mesh is stored

        :Type: str
        """,
    )

    def _get_path(self):
        """getter of path"""
        return self._path

    def _set_path(self, value):
        """setter of path"""
        check_var("path", value, "str")
        self._path = value

    path = property(
        fget=_get_path,
        fset=_set_path,
        doc=u"""Path where the mesh is stored

        :Type: str
        """,
    )

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the mesh file

        :Type: str
        """,
    )

    def _get_surf(self):
        """getter of surf"""
        return self._surf

    def _set_surf(self, value):
        """setter of surf"""
        try:  # Check the type
            check_var("surf", value, "dict")
        except CheckTypeError:
            check_var("surf", value, "pyvista.core.pointset.PolyData")
            # property can be set from a list to handle loads
        if (
            type(value) == dict
        ):  # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._surf = loads(value["serialized"].encode("ISO-8859-2"))
        else:
            self._surf = value

    surf = property(
        fget=_get_surf,
        fset=_set_surf,
        doc=u"""Pyvista object of the outer surface

        :Type: pyvista.core.pointset.PolyData
        """,
    )

    def _get_is_vtk_surf(self):
        """getter of is_vtk_surf"""
        return self._is_vtk_surf

    def _set_is_vtk_surf(self, value):
        """setter of is_vtk_surf"""
        check_var("is_vtk_surf", value, "bool")
        self._is_vtk_surf = value

    is_vtk_surf = property(
        fget=_get_is_vtk_surf,
        fset=_set_is_vtk_surf,
        doc=u"""Save the surface mesh in a vtk file

        :Type: bool
        """,
    )

    def _get_surf_path(self):
        """getter of surf_path"""
        return self._surf_path

    def _set_surf_path(self, value):
        """setter of surf_path"""
        check_var("surf_path", value, "str")
        self._surf_path = value

    surf_path = property(
        fget=_get_surf_path,
        fset=_set_surf_path,
        doc=u"""Path where the outer surface is stored

        :Type: str
        """,
    )

    def _get_surf_name(self):
        """getter of surf_name"""
        return self._surf_name

    def _set_surf_name(self, value):
        """setter of surf_name"""
        check_var("surf_name", value, "str")
        self._surf_name = value

    surf_name = property(
        fget=_get_surf_name,
        fset=_set_surf_name,
        doc=u"""Name of the outer surface file

        :Type: str
        """,
    )
