<script setup lang="ts">
import { columns } from "../../constants/tableColumns";
import { ref, onMounted, computed } from "vue";
import { IParcel } from "../../types/parcels";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "../../components/ui/table";
import Api from "../../services/api";
import InputSearch from "../../components/ui/input/InputSearch.vue";
import Skeleton from "../../components/ui/skeleton/Skeleton.vue";
import { useToast } from "../../components/ui/toast/use-toast";

const parcels = ref<IParcel[]>([]);
const loading = ref<boolean>(true);
const searchFilter = ref<string>("");
const { toast } = useToast();

const getParcels = async () => {
  try {
    const data = await Api.Parcels.list();
    parcels.value = data;
  } catch (error) {
    toast({
      title: "Error fetching parcels",
      description: "There was a problem with your request.",
      variant: "destructive",
    });
  } finally {
    loading.value = false;
  }
};

const filteredParcels = computed<IParcel[]>(() => {
  if (searchFilter.value !== "") {
    const filtered = parcels.value.filter(
      (elm) =>
        (elm.name && elm.name.toLowerCase().includes(searchFilter.value)) ||
        (elm.department && elm.department.toLowerCase().includes(searchFilter.value))
    );

    return filtered;
  }

  return parcels.value;
});

const handleSearch = (search) => {
  searchFilter.value = search;
};

onMounted(async () => getParcels());
</script>

<template>
  <div class="md:container">
    <InputSearch class="mb-28" @search="handleSearch" />
    <div
      class="flex flex-col mb-10 gap-2 max-w-full md:max-w-[653px] items-start">
      <h1 class="text-2xl font-medium text-foreground">Parcels</h1>
      <p class="text-md text-gray-500">
        View and manage all parcels in a single table.
      </p>
    </div>
    <Skeleton v-if="loading" class="h-[225px] max-w-full rounded-xl" />
    <Table v-else>
      <TableHeader>
        <TableRow>
          <TableHead
            class="w-[100px]"
            v-for="column in columns"
            :key="column.field">
            {{ column.header }}
          </TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <TableRow
          v-for="row in filteredParcels"
          :key="row.name"
          class="hover:bg-gray-100 cursor-pointer">
          <TableCell v-for="column in columns" :key="column.field">
            {{ column.render ? column.render(row[column.field]) : row[column.field] }}
          </TableCell>
        </TableRow>
        <div v-if="filteredParcels.length === 0" colspan="columns.length">
          No parcels found.
        </div>
      </TableBody>
    </Table>
  </div>
</template>
