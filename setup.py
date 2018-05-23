#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for networkx

You can install networkx with

python setup.py install
"""
from glob import glob
import os
import sys
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()

if sys.version_info[:2] < (2, 7):
    print("NetworkX requires Python 2.7 or later (%d.%d detected)." %
          sys.version_info[:2])
    sys.exit(-1)

# Write the version information.
sys.path.insert(0, 'networkx')
import release
version = release.write_versionfile()
sys.path.pop(0)

extensions = [
    Extension("networkx.algorithms.approximation.__init__", ["networkx/algorithms/approximation/__init__.py"]),
    Extension("networkx.algorithms.approximation.clique", ["networkx/algorithms/approximation/clique.py"]),
    Extension("networkx.algorithms.approximation.clustering_coefficient", ["networkx/algorithms/approximation/clustering_coefficient.py"]),
    Extension("networkx.algorithms.approximation.connectivity", ["networkx/algorithms/approximation/connectivity.py"]),
    Extension("networkx.algorithms.approximation.dominating_set", ["networkx/algorithms/approximation/dominating_set.py"]),
    Extension("networkx.algorithms.approximation.independent_set", ["networkx/algorithms/approximation/independent_set.py"]),
    Extension("networkx.algorithms.approximation.kcomponents", ["networkx/algorithms/approximation/kcomponents.py"]),
    Extension("networkx.algorithms.approximation.matching", ["networkx/algorithms/approximation/matching.py"]),
    Extension("networkx.algorithms.approximation.ramsey", ["networkx/algorithms/approximation/ramsey.py"]),
    Extension("networkx.algorithms.approximation.steinertree", ["networkx/algorithms/approximation/steinertree.py"]),
    Extension("networkx.algorithms.approximation.vertex_cover", ["networkx/algorithms/approximation/vertex_cover.py"]),

    Extension("networkx.algorithms.assortativity.__init__", ["networkx/algorithms/assortativity/__init__.py"]),
    Extension("networkx.algorithms.assortativity.connectivity", ["networkx/algorithms/assortativity/connectivity.py"]),
    Extension("networkx.algorithms.assortativity.correlation", ["networkx/algorithms/assortativity/correlation.py"]),
    Extension("networkx.algorithms.assortativity.mixing", ["networkx/algorithms/assortativity/mixing.py"]),
    Extension("networkx.algorithms.assortativity.neighbor_degree", ["networkx/algorithms/assortativity/neighbor_degree.py"]),
    Extension("networkx.algorithms.assortativity.pairs", ["networkx/algorithms/assortativity/pairs.py"]),

    Extension("networkx.algorithms.bipartite.__init__", ["networkx/algorithms/bipartite/__init__.py"]),
    Extension("networkx.algorithms.bipartite.basic", ["networkx/algorithms/bipartite/basic.py"]),
    Extension("networkx.algorithms.bipartite.centrality", ["networkx/algorithms/bipartite/centrality.py"]),
    Extension("networkx.algorithms.bipartite.cluster", ["networkx/algorithms/bipartite/cluster.py"]),
    Extension("networkx.algorithms.bipartite.covering", ["networkx/algorithms/bipartite/covering.py"]),
    Extension("networkx.algorithms.bipartite.edgelist", ["networkx/algorithms/bipartite/edgelist.py"]),
    Extension("networkx.algorithms.bipartite.generators", ["networkx/algorithms/bipartite/generators.py"]),
    Extension("networkx.algorithms.bipartite.matching", ["networkx/algorithms/bipartite/matching.py"]),
    Extension("networkx.algorithms.bipartite.matrix", ["networkx/algorithms/bipartite/matrix.py"]),
    Extension("networkx.algorithms.bipartite.projection", ["networkx/algorithms/bipartite/projection.py"]),
    Extension("networkx.algorithms.bipartite.redundancy", ["networkx/algorithms/bipartite/redundancy.py"]),
    Extension("networkx.algorithms.bipartite.spectral", ["networkx/algorithms/bipartite/spectral.py"]),

    Extension("networkx.algorithms.centrality.__init__", ["networkx/algorithms/centrality/__init__.py"]),
    Extension("networkx.algorithms.centrality.betweenness", ["networkx/algorithms/centrality/betweenness.py"]),
    Extension("networkx.algorithms.centrality.betweenness_subset", ["networkx/algorithms/centrality/betweenness_subset.py"]),
    Extension("networkx.algorithms.centrality.closeness", ["networkx/algorithms/centrality/closeness.py"]),
    Extension("networkx.algorithms.centrality.current_flow_betweenness", ["networkx/algorithms/centrality/current_flow_betweenness.py"]),
    Extension("networkx.algorithms.centrality.current_flow_betweenness_subset", ["networkx/algorithms/centrality/current_flow_betweenness_subset.py"]),
    Extension("networkx.algorithms.centrality.current_flow_closeness", ["networkx/algorithms/centrality/current_flow_closeness.py"]),
    Extension("networkx.algorithms.centrality.degree_alg", ["networkx/algorithms/centrality/degree_alg.py"]),
    Extension("networkx.algorithms.centrality.dispersion", ["networkx/algorithms/centrality/dispersion.py"]),
    Extension("networkx.algorithms.centrality.eigenvector", ["networkx/algorithms/centrality/eigenvector.py"]),
    Extension("networkx.algorithms.centrality.flow_matrix", ["networkx/algorithms/centrality/flow_matrix.py"]),
    Extension("networkx.algorithms.centrality.harmonic", ["networkx/algorithms/centrality/harmonic.py"]),
    Extension("networkx.algorithms.centrality.katz", ["networkx/algorithms/centrality/katz.py"]),
    Extension("networkx.algorithms.centrality.load", ["networkx/algorithms/centrality/load.py"]),
    Extension("networkx.algorithms.centrality.reaching", ["networkx/algorithms/centrality/reaching.py"]),
    Extension("networkx.algorithms.centrality.subgraph_alg", ["networkx/algorithms/centrality/subgraph_alg.py"]),

    Extension("networkx.algorithms.coloring.__init__", ["networkx/algorithms/coloring/__init__.py"]),
    Extension("networkx.algorithms.coloring.greedy_coloring", ["networkx/algorithms/coloring/greedy_coloring.py"]),
    Extension("networkx.algorithms.coloring.greedy_coloring_with_interchange", ["networkx/algorithms/coloring/greedy_coloring_with_interchange.py"]),

    Extension("networkx.algorithms.community.__init__", ["networkx/algorithms/community/__init__.py"]),
    Extension("networkx.algorithms.community.asyn_fluidc", ["networkx/algorithms/community/asyn_fluidc.py"]),
    Extension("networkx.algorithms.community.centrality", ["networkx/algorithms/community/centrality.py"]),
    Extension("networkx.algorithms.community.community_generators", ["networkx/algorithms/community/community_generators.py"]),
    Extension("networkx.algorithms.community.community_utils", ["networkx/algorithms/community/community_utils.py"]),
    Extension("networkx.algorithms.community.kclique", ["networkx/algorithms/community/kclique.py"]),
    Extension("networkx.algorithms.community.kernighan_lin", ["networkx/algorithms/community/kernighan_lin.py"]),
    Extension("networkx.algorithms.community.label_propagation", ["networkx/algorithms/community/label_propagation.py"]),
    Extension("networkx.algorithms.community.quality", ["networkx/algorithms/community/quality.py"]),

    Extension("networkx.algorithms.components.__init__", ["networkx/algorithms/components/__init__.py"]),
    Extension("networkx.algorithms.components.attracting", ["networkx/algorithms/components/attracting.py"]),
    Extension("networkx.algorithms.components.biconnected", ["networkx/algorithms/components/biconnected.py"]),
    Extension("networkx.algorithms.components.connected", ["networkx/algorithms/components/connected.py"]),
    Extension("networkx.algorithms.components.semiconnected", ["networkx/algorithms/components/semiconnected.py"]),
    Extension("networkx.algorithms.components.strongly_connected", ["networkx/algorithms/components/strongly_connected.py"]),
    Extension("networkx.algorithms.components.weakly_connected", ["networkx/algorithms/components/weakly_connected.py"]),

    Extension("networkx.algorithms.connectivity.__init__", ["networkx/algorithms/connectivity/__init__.py"]),
    Extension("networkx.algorithms.connectivity.connectivity", ["networkx/algorithms/connectivity/connectivity.py"]),
    Extension("networkx.algorithms.connectivity.cuts", ["networkx/algorithms/connectivity/cuts.py"]),
    Extension("networkx.algorithms.connectivity.disjoint_paths", ["networkx/algorithms/connectivity/disjoint_paths.py"]),
    Extension("networkx.algorithms.connectivity.edge_augmentation", ["networkx/algorithms/connectivity/edge_augmentation.py"]),
    Extension("networkx.algorithms.connectivity.edge_kcomponents", ["networkx/algorithms/connectivity/edge_kcomponents.py"]),
    Extension("networkx.algorithms.connectivity.kcomponents", ["networkx/algorithms/connectivity/kcomponents.py"]),
    Extension("networkx.algorithms.connectivity.kcutsets", ["networkx/algorithms/connectivity/kcutsets.py"]),
    Extension("networkx.algorithms.connectivity.stoerwagner", ["networkx/algorithms/connectivity/stoerwagner.py"]),
    Extension("networkx.algorithms.connectivity.utils", ["networkx/algorithms/connectivity/utils.py"]),

    Extension("networkx.algorithms.flow.__init__", ["networkx/algorithms/flow/__init__.py"]),
    Extension("networkx.algorithms.flow.boykovkolmogorov", ["networkx/algorithms/flow/boykovkolmogorov.py"]),
    Extension("networkx.algorithms.flow.capacityscaling", ["networkx/algorithms/flow/capacityscaling.py"]),
    Extension("networkx.algorithms.flow.dinitz_alg", ["networkx/algorithms/flow/dinitz_alg.py"]),
    Extension("networkx.algorithms.flow.edmondskarp", ["networkx/algorithms/flow/edmondskarp.py"]),
    Extension("networkx.algorithms.flow.gomory_hu", ["networkx/algorithms/flow/gomory_hu.py"]),
    Extension("networkx.algorithms.flow.maxflow", ["networkx/algorithms/flow/maxflow.py"]),
    Extension("networkx.algorithms.flow.mincost", ["networkx/algorithms/flow/mincost.py"]),
    Extension("networkx.algorithms.flow.networksimplex", ["networkx/algorithms/flow/networksimplex.py"]),
    Extension("networkx.algorithms.flow.preflowpush", ["networkx/algorithms/flow/preflowpush.py"]),
    Extension("networkx.algorithms.flow.shortestaugmentingpath", ["networkx/algorithms/flow/shortestaugmentingpath.py"]),
    Extension("networkx.algorithms.flow.utils", ["networkx/algorithms/flow/utils.py"]),

    Extension("networkx.algorithms.isomorphism.__init__", ["networkx/algorithms/isomorphism/__init__.py"]),
    Extension("networkx.algorithms.isomorphism.isomorph", ["networkx/algorithms/isomorphism/isomorph.py"]),
    Extension("networkx.algorithms.isomorphism.isomorphvf2", ["networkx/algorithms/isomorphism/isomorphvf2.py"]),
    Extension("networkx.algorithms.isomorphism.matchhelpers", ["networkx/algorithms/isomorphism/matchhelpers.py"]),
    Extension("networkx.algorithms.isomorphism.temporalisomorphvf2", ["networkx/algorithms/isomorphism/temporalisomorphvf2.py"]),
    Extension("networkx.algorithms.isomorphism.vf2userfunc", ["networkx/algorithms/isomorphism/vf2userfunc.py"]),

    Extension("networkx.algorithms.link_analysis.__init__", ["networkx/algorithms/link_analysis/__init__.py"]),
    Extension("networkx.algorithms.link_analysis.hits_alg", ["networkx/algorithms/link_analysis/hits_alg.py"]),
    Extension("networkx.algorithms.link_analysis.pagerank_alg", ["networkx/algorithms/link_analysis/pagerank_alg.py"]),

    Extension("networkx.algorithms.operators.__init__", ["networkx/algorithms/operators/__init__.py"]),
    Extension("networkx.algorithms.operators.all", ["networkx/algorithms/operators/all.py"]),
    Extension("networkx.algorithms.operators.binary", ["networkx/algorithms/operators/binary.py"]),
    Extension("networkx.algorithms.operators.product", ["networkx/algorithms/operators/product.py"]),
    Extension("networkx.algorithms.operators.unary", ["networkx/algorithms/operators/unary.py"]),

    Extension("networkx.algorithms.shortest_paths.__init__", ["networkx/algorithms/shortest_paths/__init__.py"]),
    Extension("networkx.algorithms.shortest_paths.astar", ["networkx/algorithms/shortest_paths/astar.py"]),
    Extension("networkx.algorithms.shortest_paths.dense", ["networkx/algorithms/shortest_paths/dense.py"]),
    Extension("networkx.algorithms.shortest_paths.generic", ["networkx/algorithms/shortest_paths/generic.py"]),
    Extension("networkx.algorithms.shortest_paths.unweighted", ["networkx/algorithms/shortest_paths/unweighted.py"]),
    Extension("networkx.algorithms.shortest_paths.weighted", ["networkx/algorithms/shortest_paths/weighted.py"]),

    Extension("networkx.algorithms.traversal.__init__", ["networkx/algorithms/traversal/__init__.py"]),
    Extension("networkx.algorithms.traversal.beamsearch", ["networkx/algorithms/traversal/beamsearch.py"]),
    Extension("networkx.algorithms.traversal.breadth_first_search", ["networkx/algorithms/traversal/breadth_first_search.py"]),
    Extension("networkx.algorithms.traversal.depth_first_search", ["networkx/algorithms/traversal/depth_first_search.py"]),
    Extension("networkx.algorithms.traversal.edgedfs", ["networkx/algorithms/traversal/edgedfs.py"]),

    Extension("networkx.algorithms.tree.__init__", ["networkx/algorithms/tree/__init__.py"]),
    Extension("networkx.algorithms.tree.branchings", ["networkx/algorithms/tree/branchings.py"]),
    Extension("networkx.algorithms.tree.coding", ["networkx/algorithms/tree/coding.py"]),
    Extension("networkx.algorithms.tree.mst", ["networkx/algorithms/tree/mst.py"]),
    Extension("networkx.algorithms.tree.operations", ["networkx/algorithms/tree/operations.py"]),
    Extension("networkx.algorithms.tree.recognition", ["networkx/algorithms/tree/recognition.py"]),

    Extension("networkx.algorithms.__init__", ["networkx/algorithms/__init__.py"]),
    Extension("networkx.algorithms.boundary", ["networkx/algorithms/boundary.py"]),
    Extension("networkx.algorithms.bridges", ["networkx/algorithms/bridges.py"]),
    Extension("networkx.algorithms.chains", ["networkx/algorithms/chains.py"]),
    Extension("networkx.algorithms.chordal", ["networkx/algorithms/chordal.py"]),
    Extension("networkx.algorithms.clique", ["networkx/algorithms/clique.py"]),
    Extension("networkx.algorithms.cluster", ["networkx/algorithms/cluster.py"]),
    Extension("networkx.algorithms.communicability_alg", ["networkx/algorithms/communicability_alg.py"]),
    Extension("networkx.algorithms.core", ["networkx/algorithms/core.py"]),
    Extension("networkx.algorithms.covering", ["networkx/algorithms/covering.py"]),
    Extension("networkx.algorithms.cuts", ["networkx/algorithms/cuts.py"]),
    Extension("networkx.algorithms.cycles", ["networkx/algorithms/cycles.py"]),
    Extension("networkx.algorithms.dag", ["networkx/algorithms/dag.py"]),
    Extension("networkx.algorithms.distance_measures", ["networkx/algorithms/distance_measures.py"]),
    Extension("networkx.algorithms.distance_regular", ["networkx/algorithms/distance_regular.py"]),
    Extension("networkx.algorithms.dominance", ["networkx/algorithms/dominance.py"]),
    Extension("networkx.algorithms.domninating", ["networkx/algorithms/dominating.py"]),
    Extension("networkx.algorithms.efficiency", ["networkx/algorithms/efficiency.py"]),
    Extension("networkx.algorithms.euler", ["networkx/algorithms/euler.py"]),
    Extension("networkx.algorithms.graphical", ["networkx/algorithms/graphical.py"]),
    Extension("networkx.algorithms.hierarchy", ["networkx/algorithms/hierarchy.py"]),
    Extension("networkx.algorithms.hybrid", ["networkx/algorithms/hybrid.py"]),
    Extension("networkx.algorithms.isolate", ["networkx/algorithms/isolate.py"]),
    Extension("networkx.algorithms.link_prediction", ["networkx/algorithms/link_prediction.py"]),
    Extension("networkx.algorithms.lowest_common_ancestors", ["networkx/algorithms/lowest_common_ancestors.py"]),
    Extension("networkx.algorithms.matching", ["networkx/algorithms/matching.py"]),
    Extension("networkx.algorithms.minors", ["networkx/algorithms/minors.py"]),
    Extension("networkx.algorithms.mis", ["networkx/algorithms/mis.py"]),
    Extension("networkx.algorithms.reciprocity", ["networkx/algorithms/reciprocity.py"]),
    Extension("networkx.algorithms.richclub", ["networkx/algorithms/richclub.py"]),
    Extension("networkx.algorithms.similarity", ["networkx/algorithms/similarity.py"]),
    Extension("networkx.algorithms.simple_paths", ["networkx/algorithms/simple_paths.py"]),
    Extension("networkx.algorithms.smetric", ["networkx/algorithms/smetric.py"]),
    Extension("networkx.algorithms.structuralholes", ["networkx/algorithms/structuralholes.py"]),
    Extension("networkx.algorithms.swap", ["networkx/algorithms/swap.py"]),
    Extension("networkx.algorithms.threshold", ["networkx/algorithms/threshold.py"]),
    Extension("networkx.algorithms.tournament", ["networkx/algorithms/tournament.py"]),
    Extension("networkx.algorithms.triads", ["networkx/algorithms/triads.py"]),
    Extension("networkx.algorithms.vitality", ["networkx/algorithms/vitality.py"]),
    Extension("networkx.algorithms.voronoi", ["networkx/algorithms/voronoi.py"]),
    Extension("networkx.algorithms.weiner", ["networkx/algorithms/wiener.py"]),

    Extension("networkx.classes.__init__", ["networkx/classes/__init__.py"]),
    Extension("networkx.classes.coreviews", ["networkx/classes/coreviews.py"]),
    Extension("networkx.classes.digraph", ["networkx/classes/digraph.py"]),
    Extension("networkx.classes.filters", ["networkx/classes/filters.py"]),
    Extension("networkx.classes.function", ["networkx/classes/function.py"]),
    Extension("networkx.classes.graph", ["networkx/classes/graph.py"]),
    Extension("networkx.classes.graphviews", ["networkx/classes/graphviews.py"]),
    Extension("networkx.classes.multidigraph", ["networkx/classes/multidigraph.py"]),
    Extension("networkx.classes.multigraph", ["networkx/classes/multigraph.py"]),
    Extension("networkx.classes.ordered", ["networkx/classes/ordered.py"]),
    Extension("networkx.classes.reportviews", ["networkx/classes/reportviews.py"]),

    Extension("networkx.utils.__init__", ["networkx/utils/__init__.py"]),
    Extension("networkx.utils.contextmanagers", ["networkx/utils/contextmanagers.py"]),
    Extension("networkx.utils.decorators", ["networkx/utils/decorators.py"]),
    Extension("networkx.utils.heaps", ["networkx/utils/heaps.py"]),
    Extension("networkx.utils.misc", ["networkx/utils/misc.py"]),
    Extension("networkx.utils.random_sequence", ["networkx/utils/random_sequence.py"]),
    Extension("networkx.utils.rcm", ["networkx/utils/rcm.py"]),
    Extension("networkx.utils.union_find", ["networkx/utils/union_find.py"]),

    Extension("networkx.drawing.__init__", ["networkx/drawing/__init__.py"]),
    Extension("networkx.drawing.layout", ["networkx/drawing/layout.py"]),
    Extension("networkx.drawing.nx_agraph", ["networkx/drawing/nx_agraph.py"]),
    Extension("networkx.drawing.nx_pydot", ["networkx/drawing/nx_pydot.py"]),
    Extension("networkx.drawing.nx_pylab", ["networkx/drawing/nx_pylab.py"]),

    Extension("networkx.generators.__init__", ["networkx/generators/__init__.py"]),
    Extension("networkx.generators.atlas", ["networkx/generators/atlas.py"]),
    Extension("networkx.generators.classic", ["networkx/generators/classic.py"]),
    Extension("networkx.generators.community", ["networkx/generators/community.py"]),
    Extension("networkx.generators.degree_seq", ["networkx/generators/degree_seq.py"]),
    Extension("networkx.generators.directed", ["networkx/generators/directed.py"]),
    Extension("networkx.generators.duplication", ["networkx/generators/duplication.py"]),
    Extension("networkx.generators.ego", ["networkx/generators/ego.py"]),
    Extension("networkx.generators.expanders", ["networkx/generators/expanders.py"]),
    Extension("networkx.generators.geometric", ["networkx/generators/geometric.py"]),
    Extension("networkx.generators.intersection", ["networkx/generators/intersection.py"]),
    Extension("networkx.generators.joint_degree_seq", ["networkx/generators/joint_degree_seq.py"]),
    Extension("networkx.generators.lattice", ["networkx/generators/lattice.py"]),
    Extension("networkx.generators.line", ["networkx/generators/line.py"]),
    Extension("networkx.generators.mycielski", ["networkx/generators/mycielski.py"]),
    Extension("networkx.generators.nonisomorphic_trees", ["networkx/generators/nonisomorphic_trees.py"]),
    Extension("networkx.generators.random_clustered", ["networkx/generators/random_clustered.py"]),
    Extension("networkx.generators.random_graphs", ["networkx/generators/random_graphs.py"]),
    Extension("networkx.generators.small", ["networkx/generators/small.py"]),
    Extension("networkx.generators.social", ["networkx/generators/social.py"]),
    Extension("networkx.generators.stochastic", ["networkx/generators/stochastic.py"]),
    Extension("networkx.generators.trees", ["networkx/generators/trees.py"]),
    Extension("networkx.generators.triads", ["networkx/generators/triads.py"]),

    Extension("networkx.linalg.__init__", ["networkx/linalg/__init__.py"]),
    Extension("networkx.linalg.algebraicconnectivity", ["networkx/linalg/algebraicconnectivity.py"]),
    Extension("networkx.linalg.attrmatrix", ["networkx/linalg/attrmatrix.py"]),
    Extension("networkx.linalg.graphmatrix", ["networkx/linalg/graphmatrix.py"]),
    Extension("networkx.linalg.laplacianmatrix", ["networkx/linalg/laplacianmatrix.py"]),
    Extension("networkx.linalg.modularitymatrix", ["networkx/linalg/modularitymatrix.py"]),
    Extension("networkx.linalg.spectrum", ["networkx/linalg/spectrum.py"]),

    Extension("networkx.readwrite.json_graph.__init__", ["networkx/readwrite/json_graph/__init__.py"]),
    Extension("networkx.readwrite.json_graph.adjacency", ["networkx/readwrite/json_graph/adjacency.py"]),
    Extension("networkx.readwrite.json_graph.cytoscape", ["networkx/readwrite/json_graph/cytoscape.py"]),
    Extension("networkx.readwrite.json_graph.jit", ["networkx/readwrite/json_graph/jit.py"]),
    Extension("networkx.readwrite.json_graph.node_link", ["networkx/readwrite/json_graph/node_link.py"]),
    Extension("networkx.readwrite.json_graph.tree", ["networkx/readwrite/json_graph/tree.py"]),

    Extension("networkx.readwrite.__init__", ["networkx/readwrite/__init__.py"]),
    Extension("networkx.readwrite.adjlist", ["networkx/readwrite/adjlist.py"]),
    Extension("networkx.readwrite.edgelist", ["networkx/readwrite/edgelist.py"]),
    Extension("networkx.readwrite.gexf", ["networkx/readwrite/gexf.py"]),
    Extension("networkx.readwrite.gml", ["networkx/readwrite/gml.py"]),
    Extension("networkx.readwrite.gpickle", ["networkx/readwrite/gpickle.py"]),
    Extension("networkx.readwrite.graph6", ["networkx/readwrite/graph6.py"]),
    Extension("networkx.readwrite.graphml", ["networkx/readwrite/graphml.py"]),
    Extension("networkx.readwrite.leda", ["networkx/readwrite/leda.py"]),
    Extension("networkx.readwrite.multiline_adjlist", ["networkx/readwrite/multiline_adjlist.py"]),
    Extension("networkx.readwrite.nx_shp", ["networkx/readwrite/nx_shp.py"]),
    Extension("networkx.readwrite.nx_yaml", ["networkx/readwrite/nx_yaml.py"]),
    Extension("networkx.readwrite.p2g", ["networkx/readwrite/p2g.py"]),
    Extension("networkx.readwrite.pajek", ["networkx/readwrite/pajek.py"]),
    Extension("networkx.readwrite.sparse6", ["networkx/readwrite/sparse6.py"]),

    Extension("networkx.__init__", ["networkx/__init__.py"]),
    Extension("networkx.convert", ["networkx/convert.py"]),
    Extension("networkx.convert_matrix", ["networkx/convert_matrix.py"]),
    Extension("networkx.exception", ["networkx/exception.py"]),
    Extension("networkx.relabel", ["networkx/relabel.py"]),
    Extension("networkx.release", ["networkx/release.py"]),
    Extension("networkx.version", ["networkx/version.py"]),
]

packages = ["networkx",
            "networkx.algorithms",
            "networkx.algorithms.assortativity",
            "networkx.algorithms.bipartite",
            "networkx.algorithms.node_classification",
            "networkx.algorithms.centrality",
            "networkx.algorithms.community",
            "networkx.algorithms.components",
            "networkx.algorithms.connectivity",
            "networkx.algorithms.coloring",
            "networkx.algorithms.flow",
            "networkx.algorithms.traversal",
            "networkx.algorithms.isomorphism",
            "networkx.algorithms.shortest_paths",
            "networkx.algorithms.link_analysis",
            "networkx.algorithms.operators",
            "networkx.algorithms.approximation",
            "networkx.algorithms.tree",
            "networkx.classes",
            "networkx.generators",
            "networkx.drawing",
            "networkx.linalg",
            "networkx.readwrite",
            "networkx.readwrite.json_graph",
            "networkx.tests",
            "networkx.testing",
            "networkx.utils"]

docdirbase = 'share/doc/networkx-%s' % version
# add basic documentation
data = [(docdirbase, glob("*.txt"))]
# add examples
for d in ['.',
          'advanced',
          'algorithms',
          'basic',
          '3d_drawing',
          'drawing',
          'graph',
          'javascript',
          'jit',
          'pygraphviz',
          'subclass']:
    dd = os.path.join(docdirbase, 'examples', d)
    pp = os.path.join('examples', d)
    data.append((dd, glob(os.path.join(pp, "*.txt"))))
    data.append((dd, glob(os.path.join(pp, "*.py"))))
    data.append((dd, glob(os.path.join(pp, "*.bz2"))))
    data.append((dd, glob(os.path.join(pp, "*.gz"))))
    data.append((dd, glob(os.path.join(pp, "*.mbox"))))
    data.append((dd, glob(os.path.join(pp, "*.edgelist"))))

# add the tests
package_data = {
    'networkx': ['tests/*.py'],
    'networkx.algorithms': ['tests/*.py'],
    'networkx.algorithms.assortativity': ['tests/*.py'],
    'networkx.algorithms.bipartite': ['tests/*.py'],
    'networkx.algorithms.node_classification': ['tests/*.py'],
    'networkx.algorithms.centrality': ['tests/*.py'],
    'networkx.algorithms.community': ['tests/*.py'],
    'networkx.algorithms.components': ['tests/*.py'],
    'networkx.algorithms.connectivity': ['tests/*.py'],
    'networkx.algorithms.coloring': ['tests/*.py'],
    'networkx.algorithms.flow': ['tests/*.py', 'tests/*.bz2'],
    'networkx.algorithms.isomorphism': ['tests/*.py', 'tests/*.*99'],
    'networkx.algorithms.link_analysis': ['tests/*.py'],
    'networkx.algorithms.approximation': ['tests/*.py'],
    'networkx.algorithms.operators': ['tests/*.py'],
    'networkx.algorithms.shortest_paths': ['tests/*.py'],
    'networkx.algorithms.traversal': ['tests/*.py'],
    'networkx.algorithms.tree': ['tests/*.py'],
    'networkx.classes': ['tests/*.py'],
    'networkx.generators': ['tests/*.py', 'atlas.dat.gz'],
    'networkx.drawing': ['tests/*.py'],
    'networkx.linalg': ['tests/*.py'],
    'networkx.readwrite': ['tests/*.py'],
    'networkx.readwrite.json_graph': ['tests/*.py'],
    'networkx.testing': ['tests/*.py'],
    'networkx.utils': ['tests/*.py']
}

install_requires = ['decorator>=4.1.0']
extras_require = {'all': ['numpy', 'scipy', 'pandas', 'matplotlib',
                          'pygraphviz', 'pydot', 'pyyaml', 'gdal', 'lxml','nose']}

if __name__ == "__main__":

    setup(
        name=release.name.lower(),
        version=version,
        maintainer=release.maintainer,
        maintainer_email=release.maintainer_email,
        author=release.authors['Hagberg'][0],
        author_email=release.authors['Hagberg'][1],
        description=release.description,
        keywords=release.keywords,
        long_description=release.long_description,
        license=release.license,
        platforms=release.platforms,
        url=release.url,
        download_url=release.download_url,
        classifiers=release.classifiers,
        packages=packages,
        data_files=data,
        package_data=package_data,
        install_requires=install_requires,
        extras_require=extras_require,
        test_suite='nose.collector',
        tests_require=['nose>=0.10.1'],
        zip_safe=False,
        ext_modules=cythonize(extensions)
    )
