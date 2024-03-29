### A Pluto.jl notebook ###
# v0.19.17

using Markdown
using InteractiveUtils

# ╔═╡ 8c343d9a-7797-11ed-1c63-e3a14c73b033
input = readlines("/home/aj/cojects/aoc/aoc18/day1.txt")

# ╔═╡ e9fc8aea-d064-4473-bc22-fb357babd610
added = 0

# ╔═╡ 29b93667-afda-4efa-88e0-478630888bd5
reacurring = []

# ╔═╡ 949b47fe-f0f0-49cc-93a3-6bd70f02587d
# Part 1 aoc 2018
begin
	for i in input
		x = parse(Int, i)
		added = added + x
	end
	print(added)
end
	


# ╔═╡ c7f58c9a-4e62-4629-b806-fcd1e6aa94d8
begin
	for i in input
		x = parse(Int, i)
		added = added + x
		push!(reacurring, added)

		if in(added, reacurring)
			println(added)
		end
	end
	println(added)
	#println(reacurring)
end
	

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

julia_version = "1.8.3"
manifest_format = "2.0"
project_hash = "da39a3ee5e6b4b0d3255bfef95601890afd80709"

[deps]
"""

# ╔═╡ Cell order:
# ╠═8c343d9a-7797-11ed-1c63-e3a14c73b033
# ╠═e9fc8aea-d064-4473-bc22-fb357babd610
# ╠═29b93667-afda-4efa-88e0-478630888bd5
# ╠═949b47fe-f0f0-49cc-93a3-6bd70f02587d
# ╠═c7f58c9a-4e62-4629-b806-fcd1e6aa94d8
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
