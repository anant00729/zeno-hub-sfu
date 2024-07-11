<script lang="ts">
	import type { Image } from '$lib/instance-views/schema.js';
	import { mdiArrowExpand, mdiClose } from '@mdi/js';

	export let data: string;
	export let spec: Image;
	export let entry_data: { [key: string]: any }; 

	const widthMap = {
		small: 'w-48',
		medium: 'w-64',
		large: 'w-96',
		full: 'w-full'
	};

	let showPopup = false;
	let imageElement: HTMLImageElement | null = null;

	function calculatePosition(box: number[], imgWidth: number, imgHeight: number) {
		const [xmin,ymin,xmax,ymax] = box;

		const scaleX = imgWidth / entry_data.width;
		const scaleY = imgHeight / entry_data.height;
		let left = xmin * scaleX;
		let top = ymin * scaleY;
		let width = (xmax - xmin) * scaleX;
		let height = (ymax - ymin) * scaleY;

		const result = {
			left: `${left}px`,
			top: `${top}px`,
			width: `${width}px`,
			height: `${height}px`
		};
		return result;
	}
</script>

<div class="relative" style="width: 250px; height: 250px; margin: auto;">
	<img
		bind:this={imageElement}
		class={spec.maxWidth ? widthMap[spec.maxWidth] : ''}
		src={data}
		alt="Image thumbnail for instance {data}"
	/>
	<button
		class=""
		on:click={(e) => {
			showPopup = true;
			e.preventDefault();
		}}
	>
		<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-6 fill-grey-darker">
			<path d={mdiArrowExpand} />
		</svg>
	</button>
	{#if entry_data.gt_boxes && entry_data.d_boxes}
		{#each entry_data.gt_boxes as gt_value, i}
		<div
			class="absolute border-2 border-green-500"
			style={`left: ${calculatePosition(gt_value, 250, 187.29).left}; top: ${calculatePosition(gt_value, 250, 187.29).top}; width: ${calculatePosition(gt_value, 250, 187.29).width}; height: ${calculatePosition(gt_value, 250, 187.29).height}; border: 2px solid green;`}
		></div>
		{/each}
		{#each entry_data.d_boxes as d_result, i}
		<div
			class="absolute border-2 border-red-500"
			style={`left: ${calculatePosition(d_result, 250, 187.29).left}; top: ${calculatePosition(d_result, 250, 187.29).top}; width: ${calculatePosition(d_result, 250, 187.29).width}; height: ${calculatePosition(d_result, 250, 187.29).height}; border: 2px solid red;`}
		></div>
		{/each}
	{/if}
</div>

{#if showPopup}
	<div
		id="fullscreenModal"
		class="bg-gray-500 fixed inset-0 z-50 flex items-center justify-center bg-opacity-75 p-4"
	>
		<div class="relative w-full max-w-2xl rounded-lg bg-white p-6 shadow-xl">
			<button
				on:click={() => (showPopup = false)}
				class="absolute right-0 top-0 mr-4 mt-4 rounded-md p-1 hover:bg-primary-ligther"
			>
				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-6 fill-grey-darker">
					<path d={mdiClose} />
				</svg>
			</button>
			<img src={data} alt="Image thumbnail for instance {data}" />
			{#if entry_data.gt_boxes && entry_data.d_boxes}
				{#each entry_data.gt_boxes as gt_value, i}
				<div
					class="absolute border-2 border-green-500"
					style={`left: ${calculatePosition(gt_value, 636, 502).left}; top: ${calculatePosition(gt_value, 636, 502).top}; width: ${calculatePosition(gt_value, 636, 502).width}; height: ${calculatePosition(gt_value,636, 502).height}; border: 2px solid green;`}
				></div>
				{/each}
				{#each entry_data.d_boxes as d_result, i}
				<div
					class="absolute border-2 border-red-500"
					style={`left: ${calculatePosition(d_result, 636, 502).left}; top: ${calculatePosition(d_result, 636, 502).top}; width: ${calculatePosition(d_result, 636, 502).width}; height: ${calculatePosition(d_result, 636, 502).height}; border: 2px solid red;`}
				></div>
				{/each}
			{/if}
		</div>
	</div>
{/if}
