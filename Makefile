clean:
	rm -rf build; \
	rm -f networkx/*.c networkx/*.so networkx/*.pyc; \
	rm -f networkx/algorithms/*.c networkx/algorithms/*.so networkx/algorithms/*.pyc; \
	rm -f networkx/algorithms/approximation/*.c networkx/algorithms/approximation/*.so networkx/algorithms/approximation/*.pyc; \
	rm -f networkx/algorithms/assortativity/*.c networkx/algorithms/assortativity/*.so networkx/algorithms/assortativity/*.pyc; \
	rm -f networkx/algorithms/bipartite/*.c networkx/algorithms/bipartite/*.so networkx/algorithms/bipartite/*.pyc; \
	rm -f networkx/algorithms/centrality/*.c networkx/algorithms/centrality/*.so networkx/algorithms/centrality/*.pyc; \
	rm -f networkx/algorithms/coloring/*.c networkx/algorithms/coloring/*.so networkx/algorithms/coloring/*.pyc; \
	rm -f networkx/algorithms/community/*.c networkx/algorithms/community/*.so networkx/algorithms/community/*.pyc; \
	rm -f networkx/algorithms/components/*.c networkx/algorithms/components/*.so networkx/algorithms/components/*.pyc; \
	rm -f networkx/algorithms/connectivity/*.c networkx/algorithms/connectivity/*.so networkx/algorithms/connectivity/*.pyc; \
	rm -f networkx/algorithms/flow/*.c networkx/algorithms/flow/*.so networkx/algorithms/flow/*.pyc; \
	rm -f networkx/algorithms/isomorphism/*.c networkx/algorithms/isomorphism/*.so networkx/algorithms/isomorphism/*.pyc; \
	rm -f networkx/algorithms/link_analysis/*.c networkx/algorithms/link_analysis/*.so networkx/algorithms/link_analysis/*.pyc; \
	rm -f networkx/algorithms/operators/*.c networkx/algorithms/operators/*.so networkx/algorithms/operators/*.pyc; \
	rm -f networkx/algorithms/shortest_paths/*.c networkx/algorithms/shortest_paths/*.so networkx/algorithms/shortest_paths/*.pyc; \
	rm -f networkx/algorithms/traversal/*.c networkx/algorithms/traversal/*.so networkx/algorithms/traversal/*.pyc; \
	rm -f networkx/algorithms/tree/*.c networkx/algorithms/tree/*.so networkx/algorithms/tree/*.pyc; \
	rm -f networkx/classes/*.c networkx/classes/*.so networkx/classes/*.pyc; \
	rm -f networkx/drawing/*.c networkx/drawing/*.so networkx/drawing/*.pyc; \
	rm -f networkx/generators/*.c networkx/generators/*.so networkx/generators/*.pyc; \
	rm -f networkx/linalg/*.c networkx/linalg/*.so networkx/linalg/*.pyc; \
	rm -f networkx/readwrite/*.c networkx/readwrite/*.so networkx/readwrite/*.pyc; \
	rm -f networkx/readwrite/json_graph/*.c networkx/readwrite/json_graph/*.so networkx/readwrite/json_graph/*.pyc; \
	rm -f networkx/utils/*.c networkx/utils/*.so networkx/utils/*.pyc;