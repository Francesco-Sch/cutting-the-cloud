import { atom } from "nanostores";

export const active = atom(true);
export let temperatures = atom([
	{
		temperature_limit: 25,
		visible: false,
	},
]);
